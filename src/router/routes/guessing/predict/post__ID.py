import typing
import time


import fastapi


import src.service.guessing_service
import src.schema.base_schema


router = fastapi.APIRouter()


class OutPredictGuessing(src.schema.base_schema.Response):
    is_correct: typing.Union[bool, None] = None


@router.post("/{guessing_id}")
def predict_guessing(guessing_id: str, predicted_value: typing.Annotated[str, fastapi.Form(max_length=1)]):
    predicted_value = predicted_value.lower()

    is_success, guessing_inst, error = src.service.guessing_service.get_guessing_by_id(guessing_id=guessing_id)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message=f"server error: {error.args}",
                code=1,
            ).model_dump(),
            status_code=500,
        )

    if is_success == False or guessing_inst == None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="gagal mendapatkan guessing",
                code=2,
            ).model_dump(),
            status_code=400,
        )

    if guessing_inst.predicted_value != None or guessing_inst.predicted_at != None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="tebakan sudah dilakukan",
                code=3,
            ).model_dump(),
            status_code=400,
        )

    is_correct = guessing_inst.actual_value == predicted_value

    is_success, error = src.service.guessing_service.predict_guessing_by_id(guessing_id=guessing_id, predicted_value=predicted_value)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message=f"server error: {error.args}",
                code=4,
            ).model_dump(),
            status_code=500,
        )

    if is_success == False:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="gagal memprediksi",
                code=5,
            ).model_dump(),
            status_code=400,
        )

    return fastapi.responses.JSONResponse(
        content=OutPredictGuessing(
            message="berhasil memprediksi",
            code=0,
            is_correct=is_correct,
        ).model_dump(),
        status_code=200,
    )
