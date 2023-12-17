import os


import uuid
import fastapi


from . import routes
from .. import config, service
import src.config.logger
import src.router.routes.article.get__
import src.router.routes.article.get__current
import src.router.routes.article.get__ID
import src.router.routes.article.post__
import src.router.routes.article.patch__ID
import src.router.routes.article.delete__ID
import src.router.routes.user.token.post__
import src.router.routes.user.register.post__
import src.router.routes.check_email_availability.post__
import src.router.routes.check_username_availability.post__
import src.router.routes.prediction.post__multi
import src.router.routes.prediction.post__feedback
import src.service.get_backend_information
import src.service.write_image
import src.service.predict
import src.router.routes.guessing.multi.new.get__
import src.router.routes.guessing.multi.predict.post__ID
import src.router.routes.guessing.multi.files.get__ID

__article_router = fastapi.APIRouter(prefix="/article")
__article_router.include_router(router=src.router.routes.article.get__.router)
__article_router.include_router(router=src.router.routes.article.get__current.router)
__article_router.include_router(router=src.router.routes.article.get__ID.router)
__article_router.include_router(router=src.router.routes.article.post__.router)
__article_router.include_router(router=src.router.routes.article.patch__ID.router)
__article_router.include_router(router=src.router.routes.article.delete__ID.router)

__user_router = fastapi.APIRouter(prefix="/user")
__user_router.include_router(prefix="/login", router=src.router.routes.user.token.post__.router)
__user_router.include_router(prefix="/register", router=src.router.routes.user.register.post__.router)


__check_email_availability_router = fastapi.APIRouter(prefix="/check-email-availability")
__check_email_availability_router.include_router(router=src.router.routes.check_email_availability.post__.router)

__check_username_availability_router = fastapi.APIRouter(prefix="/check-username-availability")
__check_username_availability_router.include_router(router=src.router.routes.check_username_availability.post__.router)

__prediction_multi = fastapi.APIRouter(prefix="/prediction")
__prediction_multi.include_router(router=src.router.routes.prediction.post__multi.router)
__prediction_multi.include_router(router=src.router.routes.prediction.post__feedback.router)

import src.router.routes.guessing.new.get__
import src.router.routes.guessing.file.get__
import src.router.routes.guessing.predict.post__ID

__guessing_router = fastapi.APIRouter(prefix="/guessing")
__guessing_router.include_router(prefix="/new", router=src.router.routes.guessing.new.get__.router)
__guessing_router.include_router(prefix="/file", router=src.router.routes.guessing.file.get__.router)
__guessing_router.include_router(prefix="/predict", router=src.router.routes.guessing.predict.post__ID.router)

__multi_guessing_router = fastapi.APIRouter(prefix="/multi-guessing")
__multi_guessing_router.include_router(prefix="/new", router=src.router.routes.guessing.multi.new.get__.router)
__multi_guessing_router.include_router(prefix="/predict", router=src.router.routes.guessing.multi.predict.post__ID.router)
__multi_guessing_router.include_router(prefix="/files", router=src.router.routes.guessing.multi.files.get__ID.router)


router = fastapi.APIRouter()
router.include_router(router=__article_router)
router.include_router(router=__user_router)
router.include_router(router=__check_email_availability_router)
router.include_router(router=__check_username_availability_router)
router.include_router(router=__prediction_multi)
router.include_router(router=__guessing_router)
router.include_router(router=__multi_guessing_router)


@router.get("/")
def backend_information(request: fastapi.Request):
    """
    Get backend information
    """

    src.config.logger.logger.info(f"{request.client.host} accessing {request.url.path}")

    return src.service.get_backend_information.get_backend_information()


@router.post("/semaphores/predict", deprecated=True)
def predict_image(file: fastapi.UploadFile, request: fastapi.Request):
    """
    Prediksi gambar
    """

    src.config.logger.logger.info(f"{request.client.host} accessing {request.url.path}")

    file_id = uuid.uuid4()
    filepath = f"assets/uploads/{file_id.hex}.jpg"

    src.service.write_image.write_image(file, filepath)

    return src.service.predict.predict_image(filepath)


@router.post("/semaphores/predict/multi", deprecated=True)
def predict_images(files: list[fastapi.UploadFile]):
    """
    Prediksi beberapa gambar sekaligus
    """

    file_id = uuid.uuid4()

    all_filepath: list[str] = []
    for idx, file in enumerate(files):
        filepath = f"assets/uploads/{file_id.hex}-{idx}.jpg"

        src.service.write_image.write_image(file, filepath)

        all_filepath.append(filepath)

    predictionMultiOut = src.service.predict.predict_multi_image(all_filepath)

    return predictionMultiOut


@router.get("/a/{filename}")
def get_uploaded_image(filename: str):
    filepath = f"assets/uploads/{filename}"
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return fastapi.responses.FileResponse(filepath, media_type="image/jpeg")

    return {}
