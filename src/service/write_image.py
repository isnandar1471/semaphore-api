import shutil


import fastapi


import src.config.logger


def write_image(file: fastapi.UploadFile, filepath: str):
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        src.config.logger.logger.info(f"'{filepath}' created")
