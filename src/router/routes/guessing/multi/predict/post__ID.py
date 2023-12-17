import fastapi
import typing


import src.orm.multi_guessing
import src.service.multi_guessing_service
import src.schema.base_schema


router = fastapi.APIRouter()


@router.post("/{multi_guessing_id}")
def predict_multi_guessing(multi_guessing_id: str, predicted_value: typing.Annotated[str, fastapi.Form()]):
    is_success, multi_guessing_inst, error = src.service.multi_guessing_service.get_multi_guessing_by_id(multi_guessing_id=multi_guessing_id)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message=f"server error: {error.args}",
                code=1,
            ).model_dump(),
            status_code=500,
        )

    if is_success == False or multi_guessing_inst == None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="gagal mendapatkan multi guessing",
                code=2,
            ).model_dump(),
            status_code=400,
        )

    if multi_guessing_inst.predicted_value != None or multi_guessing_inst.predicted_at != None:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="tebakan sudah dilakukan",
                code=3,
            ).model_dump(),
            status_code=400,
        )

    is_success, error = src.service.multi_guessing_service.predict_multi_guessing_by_id(multi_guessing_id=multi_guessing_id, predicted_value=predicted_value)

    return fastapi.responses.JSONResponse(
        content=src.schema.base_schema.Response(
            message="sukses",
            code=0,
        ).model_dump(),
        status_code=200,
    )
