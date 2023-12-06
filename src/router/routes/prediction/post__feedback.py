import typing
import time
import http


import jwt
import sqlalchemy
import fastapi

import src.config.database
import src.orm.prediction
import src.orm.user
import src.config.environment
import src.schema.base_schema
import src.config.credential


router = fastapi.APIRouter()


@router.post("/feedback/")
def feedback_prediction(
    prediction_id: typing.Annotated[str, fastapi.Form()],
    user_feedback: typing.Annotated[src.orm.prediction.user_feedback_enum, fastapi.Form()],
    user_feedback_detail: typing.Annotated[str, fastapi.Form(max_length=255)],
    x_apikey: typing.Annotated[str, fastapi.Header(alias="X-API-KEY")],
):
    session = src.config.database.SESSION_MAKER()

    payload: src.config.credential.PayloadStructure
    try:
        pl = jwt.decode(
            jwt=x_apikey.encode(),
            key=src.config.environment.APP_JWT_SECRET.encode(),
            algorithms=["HS256"],
        )

        payload = src.config.credential.PayloadStructure.model_validate(pl)
    except jwt.exceptions.ExpiredSignatureError as e:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="X-API-KEY is expired",
                code=1,
            ).model_dump(),
            status_code=http.HTTPStatus.UNAUTHORIZED,
        )
    except Exception as e:
        print("🚀 ~ file: post__feedback.py:47 ~ e:", e)
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="X-API-KEY doesnt valid",
                code=2,
            ).model_dump(),
            status_code=http.HTTPStatus.UNAUTHORIZED,
        )

    try:
        session.begin()

        user_inst = session.query(src.orm.user.UserOrm).filter(src.orm.user.UserOrm.username == payload.username).first()
        if user_inst == None:
            return fastapi.responses.JSONResponse(
                content=src.schema.base_schema.Response(
                    message="user not found",
                    code=3,
                ).model_dump(),
                status_code=http.HTTPStatus.BAD_REQUEST,
            )

        prediction_inst = session.query(src.orm.prediction.PredictionOrm).filter(src.orm.prediction.PredictionOrm.id == prediction_id).filter(src.orm.prediction.PredictionOrm.user_id == user_inst.id).first()

        if prediction_inst == None:
            return fastapi.responses.JSONResponse(
                content=src.schema.base_schema.Response(
                    message="prediction not found",
                    code=4,
                ).model_dump(),
                status_code=http.HTTPStatus.BAD_REQUEST,
            )

        if prediction_inst.feedbacked_at != None:
            return fastapi.responses.JSONResponse(
                content=src.schema.base_schema.Response(
                    message="prediction already feedbacked",
                    code=5,
                ).model_dump(),
                status_code=http.HTTPStatus.BAD_REQUEST,
            )

        prediction_inst.user_feedback = user_feedback.value
        prediction_inst.user_feedback_detail = user_feedback_detail
        prediction_inst.feedbacked_at = time.time()

        session.commit()
    except Exception as e:
        session.rollback()
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message=f"server error: {e.args}",
                code=6,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )
    finally:
        session.close()

    return fastapi.responses.JSONResponse(
        content=src.schema.base_schema.Response(
            message="success",
            code=0,
        ).model_dump(),
        status_code=http.HTTPStatus.OK,
    )
