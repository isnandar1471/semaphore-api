import json
import typing
import time


import uuid
import fastapi
import jwt


import src.orm.guessing
import src.schema.base_schema
import src.config.database
import src.service.guessing_service
import src.service.user_service
import src.config.credential
import src.config.environment


router = fastapi.APIRouter()


class OutNewGuessing(src.schema.base_schema.Response):
    data: typing.Optional[src.orm.guessing.GuessingSchema] = None


@router.get("/")
def new_guessing(x_apikey: typing.Annotated[typing.Union[str, None], fastapi.Header(alias="X-API-KEY")] = None):
    payload: typing.Union[src.config.credential.PayloadStructure, None] = None
    if x_apikey != None:
        try:
            pl = jwt.decode(
                jwt=x_apikey.encode(),
                key=src.config.environment.APP_JWT_SECRET.encode(),
                algorithms=["HS256"],
            )
            payload = src.config.credential.PayloadStructure.model_validate(pl)
        except jwt.exceptions.ExpiredSignatureError as e:
            return {
                "message": "X-API-KEY is expired",
                "code": 1,
            }
        except Exception as e:
            print("🚀 ~ file: post__multi.py:43 ~ e:", e)
            return {
                "message": "X-API-KEY doesnt valid",
                "code": 2,
            }

    src.service.user_service.find_user_by_username(username=payload)

    error, choosed_char, arr_choosed_filepath = src.service.guessing_service.random_file()

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutNewGuessing(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=500,
        )

    guessing_id = uuid.uuid4()
    is_success, guessing_inst, error = src.service.guessing_service.new_guessing_from_param(
        filepath=json.dumps(arr_choosed_filepath),
        actual_value=choosed_char,
        id=guessing_id,
        user_id=None,
        created_at=time.time(),
        predicted_value=None,
        predicted_at=None,
        updated_at=None,
    )

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutNewGuessing(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=500,
        )

    if is_success == False or guessing_inst == None:
        return fastapi.responses.JSONResponse(
            content=OutNewGuessing(
                message="gagal membuat tebakan",
                code=2,
                data=None,
            ).model_dump(),
            status_code=400,
        )

    data: typing.Union[src.orm.guessing.GuessingSchema, None] = None
    try:
        data = src.orm.guessing.GuessingSchema.model_validate(guessing_inst)
    except Exception as e:
        return fastapi.responses.JSONResponse(
            content=OutNewGuessing(
                message=f"server error: {e.args}",
                code=3,
                data=None,
            ).model_dump(),
            status_code=500,
        )

    return fastapi.responses.JSONResponse(
        content=OutNewGuessing(
            message="berhasil membuat tebakan",
            code=0,
            data=data,
        ).model_dump(),
        status_code=200,
    )
