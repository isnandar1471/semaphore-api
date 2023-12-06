import os
import json
import typing


import fastapi


import src.service.guessing_service
import src.schema.base_schema
import src.config.constant

router = fastapi.APIRouter()


@router.get(
    "/{guessing_id}",
)
def get_file_guessing(guessing_id: str):
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
                message="gagal mendapatkan tebakan",
                code=2,
            ).model_dump(),
            status_code=400,
        )

    list_of_path: typing.List[str]
    try:
        list_of_path = json.loads(guessing_inst.filepath)
    except Exception as e:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message=f"server error: {e.args}",
                code=3,
            ).model_dump(),
            status_code=500,
        )

    absolute_filepath = os.path.join(src.config.constant.GUESSING_DIRPATH, *list_of_path)

    if os.path.exists(absolute_filepath) == False:
        return fastapi.responses.JSONResponse(
            content=src.schema.base_schema.Response(
                message="file tidak ditemukan",
                code=3,
            ).model_dump(),
            status_code=400,
        )

    return fastapi.responses.FileResponse(
        absolute_filepath,
        filename=f"{guessing_id}{os.path.splitext(absolute_filepath)[1]}",
    )
