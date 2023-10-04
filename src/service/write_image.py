import shutil


import fastapi


from ..config import logger


def write_image(file: fastapi.UploadFile, filepath: str):
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        logger.logger.info(f"'{filepath}' created")
