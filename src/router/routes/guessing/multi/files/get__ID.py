import typing
import time
import os.path
import random


import uuid
import fastapi
import jwt


import src.orm.multi_guessing
import src.schema.base_schema
import src.service.multi_guessing_service
import src.service.user_service
import src.config.credential
import src.config.environment
import src.orm.user
import src.config.constant


router = fastapi.APIRouter()


@router.get("/{multi_guessing_id}/{char_index}")
def get_random_file(multi_guessing_id: str, char_index: int):
    is_success, multi_guessing_inst, error = src.service.multi_guessing_service.get_multi_guessing_by_id(multi_guessing_id=multi_guessing_id)

    if is_success == True and multi_guessing_inst == None:
        return fastapi.responses.JSONResponse(
            content={
                "message": "Multi Guessing not found",
                "code": 1,
            },
            status_code=400,
        )

    if error != None:
        return fastapi.responses.JSONResponse(
            content={
                "message": error.args,
                "code": 2,
            },
            status_code=500,
        )

    word = multi_guessing_inst.actual_value

    char: str
    try:
        char = word[char_index]
    except IndexError as e:
        return fastapi.responses.JSONResponse(
            content={
                "message": "Index out of range",
                "code": 3,
            },
            status_code=400,
        )

    char_dir = os.path.join(src.config.constant.GUESSING_DIRPATH, char.lower())
    random_file = random.choice(os.listdir(char_dir))
    random_file = os.path.join(char_dir, random_file)

    return fastapi.responses.FileResponse(
        path=random_file,
        status_code=200,
    )
