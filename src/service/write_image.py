import shutil
import typing

import fastapi
import PIL.Image

import src.config.logger


def write_image(file: fastapi.UploadFile, filepath: str) -> typing.Tuple[bool, typing.Union[Exception, None]]:
    is_success: bool = False
    error: typing.Union[Exception, None] = None
    try:
        PIL.Image.open(file.file).resize((128, 256)).save(filepath)
        is_success = True

        src.config.logger.logger.info(f"'{filepath}' created")
    except Exception as e:
        error = e

        src.config.logger.logger.error(f"failed to write image: {e}")

    # with open(filepath, "wb") as buffer:
    #     shutil.copyfileobj(file.file, buffer)

    return is_success, error
