import typing
import time


import uuid
import fastapi
import jwt
import random

import src.orm.multi_guessing
import src.schema.base_schema
import src.service.multi_guessing_service
import src.service.user_service
import src.config.credential
import src.config.environment
import src.orm.user
import src.config.constant

router = fastapi.APIRouter()


class OutNewMultiGuessing(src.schema.base_schema.Response):
    data: typing.Optional[src.orm.multi_guessing.MultiGuessingSchema] = None


@router.get("/")
def new_multi_guessing(x_apikey: typing.Annotated[typing.Union[str, None], fastapi.Header(alias="X-API-KEY")] = None):
    payload: typing.Union[src.config.credential.PayloadStructure, None] = None
    user_inst: typing.Union[src.orm.user.UserSchema, None] = None
    if x_apikey != None:
        try:
            pl = jwt.decode(
                jwt=x_apikey.encode(),
                key=src.config.environment.APP_JWT_SECRET.encode(),
                algorithms=["HS256"],
            )
            payload = src.config.credential.PayloadStructure.model_validate(pl)
        except jwt.exceptions.ExpiredSignatureError as e:
            return fastapi.responses.JSONResponse(
                content=OutNewMultiGuessing(
                    message="X-API-KEY is expired",
                    code=1,
                    data=None,
                ).model_dump(),
                status_code=400,
            )
        except Exception as e:
            return fastapi.responses.JSONResponse(
                content=OutNewMultiGuessing(
                    message="X-API-KEY doesnt valid",
                    code=2,
                    data=None,
                ).model_dump(),
                status_code=400,
            )

        is_success, user, error = src.service.user_service.find_user_by_username(username=payload.username)
        user_inst = user

    word: str
    try:
        word = random.choice(src.config.constant.LIST_OF_WORDS).upper()
    except Exception as e:
        return fastapi.responses.JSONResponse(
            content=OutNewMultiGuessing(
                message="gagal membuat tebakan",
                code=1,
                data=None,
            ).model_dump(),
            status_code=400,
        )

    multi_guessing_id = uuid.uuid4()
    multi_guessing_inst = src.orm.multi_guessing.MultiGuessingOrm(
        actual_value=word,
        id=str(multi_guessing_id),
        user_id=str(user_inst.id) if user_inst != None else None,
        created_at=time.time(),
        predicted_value=None,
        predicted_at=None,
        updated_at=None,
    )
    is_success, instant, error = src.service.multi_guessing_service.new_multi_guessing_from_instance(multi_guessing_inst=multi_guessing_inst)

    if is_success == False and instant == None and error != None:
        return fastapi.responses.JSONResponse(
            content=OutNewMultiGuessing(
                message=f"gagal membuat tebakan: {str(error.args)}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=400,
        )

    return fastapi.responses.JSONResponse(
        content=OutNewMultiGuessing(
            message="berhasil membuat tebakan",
            code=0,
            data=src.orm.multi_guessing.MultiGuessingSchema.model_validate(instant),
        ).model_dump(),
        status_code=200,
    )
