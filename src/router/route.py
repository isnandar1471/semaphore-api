import os
import datetime
import typing
import uuid


import fastapi


from ..service import article_service, get_backend_information, predict, write_image, mapping
from ..config import logger


router = fastapi.APIRouter()


@router.get("/")
def backend_information(request: fastapi.Request):
    """
    Get backend information
    """

    logger.logger.info(f"{request.client.host} accessing {request.url.path}")

    return get_backend_information.get_backend_information()


@router.post("/semaphores/predict")
def predict_image(file: fastapi.UploadFile, request: fastapi.Request):
    """
    Prediksi gambar
    """

    logger.logger.info(f"{request.client.host} accessing {request.url.path}")

    current_datetime = datetime.datetime.now()
    formated_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S %f")
    filepath = f"assets/uploads/{formated_datetime}.jpg"

    write_image.write_image(file, filepath)

    return predict.predict_image(filepath)


@router.post("/semaphores/predict/multi")
def predict_images(files: list[fastapi.UploadFile]):
    """
    Prediksi beberapa gambar sekaligus
    """

    file_id = uuid.uuid4()

    all_filepath: list[str] = []
    for idx, file in enumerate(files):
        filepath = f"assets/uploads/{file_id.hex} {idx}.jpg"

        write_image.write_image(file, filepath)

        all_filepath.append(filepath)

    predictionMultiOut = predict.predict_multi_image(all_filepath)

    return predictionMultiOut


@router.get("/a/{filename}")
def get_uploaded_image(filename: str):
    filepath = f"assets/uploads/{filename}"
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return fastapi.responses.FileResponse(filepath, media_type="image/jpeg")

    return {}


@router.get("/article")
def get_all_article():
    all_articles = article_service.select_all()

    all_articles = list(map(mapping.article_out, all_articles))
    return all_articles


@router.get("/article/current")
def get_latest_article(total: int = 5):
    latest_article = article_service.select_latest_article(total)

    latest_article = list(map(mapping.article_out, latest_article))

    return latest_article


@router.get("/article/{id}")
def get_article_by_id(id: str):
    current_article = article_service.select_one_by_id(uuid.UUID(hex=id))

    if not current_article:
        return {"failed": "failed"}

    current_article = mapping.article_out(current_article)

    return {"success": "success", "article": current_article}


@router.post("/article")
def post_article(
    title: typing.Annotated[str, fastapi.Form()],
    cover_url: typing.Annotated[str, fastapi.Form()],
    description: typing.Annotated[str, fastapi.Form()],
    article_url: typing.Annotated[str, fastapi.Form()],
):
    id = article_service.insert(
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
    )

    if not id:
        return {
            "failed": True,
        }

    return {
        "success": True,
        "id": id.hex,
    }


@router.patch("/article/{id}")
def update_article_by_id(
    id: str,
    title: typing.Annotated[str | None, fastapi.Form()] = None,
    cover_url: typing.Annotated[str | None, fastapi.Form()] = None,
    description: typing.Annotated[str | None, fastapi.Form()] = None,
    article_url: typing.Annotated[str | None, fastapi.Form()] = None,
):
    is_success = article_service.update_one_by_id(
        uuid.UUID(hex=id),
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
    )

    return is_success


@router.delete("/article/{id}")
def delete_article_by_id(id: str):
    is_success = article_service.delete_by_id(uuid.UUID(hex=id))

    return is_success
