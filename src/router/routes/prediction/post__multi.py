import time
import http
import typing
import uuid
import os


import fastapi
import fastapi.security
import caseconverter
import jwt
import pydantic.tools

import src.schema.base_schema
import src.config.database
import src.config.logger
import src.config.environment
import src.service.write_image
import src.service.predict
import src.config.credential
import src.orm.prediction
import src.orm.prediction_item
import src.orm.user


router = fastapi.APIRouter()


@router.post("/multi")
def predict_images(files: typing.List[fastapi.UploadFile] = [], x_apikey: typing.Annotated[typing.Union[str, None], fastapi.Header(alias="X-API-KEY")] = None):
    """
    Prediksi beberapa gambar sekaligus
    """

    payload: typing.Union[src.config.credential.PayloadStructure, None] = None
    if x_apikey != None:
        try:
            pl = jwt.decode(
                jwt=x_apikey.encode(),
                key=src.config.environment.APP_JWT_SECRET.encode(),
                algorithms=["HS256"],
            )
            payload = src.config.credential.PayloadStructure.model_validate(pl)
        except jwt.exceptions.ExpiredSignatureError as e:
            return {
                "message": "X-API-KEY is expired",
                "code": 1,
            }
        except Exception as e:
            print("🚀 ~ file: post__multi.py:43 ~ e:", e)
            return {
                "message": "X-API-KEY doesnt valid",
                "code": 2,
            }

    file_id = uuid.uuid4()

    all_filepath: list[str] = []
    for idx, file in enumerate(files):
        filepath = f"assets/uploads/{file_id}_{idx}_{caseconverter.snakecase(file.filename)}.jpg"

        src.service.write_image.write_image(file, filepath)

        all_filepath.append(filepath)

    predictionMultiOut = src.service.predict.predict_multi_image(all_filepath)

    if payload != None:
        session = src.config.database.SESSION_MAKER()
        try:
            session.begin()

            user_inst = session.query(src.orm.user.UserOrm).filter(src.orm.user.UserOrm.username == payload.username).first()

            prediction_inst = src.orm.prediction.PredictionOrm(
                id=uuid.uuid4(),
                user_id=user_inst.id if user_inst != None else None,
                model_name="kagglenotebook_mdl-vgg16_2023-06-23@18-11-41.hdf5",
                user_feedback=None,
                user_feedback_detail=None,
                feedbacked_at=None,
                requested_at=time.time(),
            )

            session.add(prediction_inst)

            prediction_items: typing.List[src.orm.prediction_item.PredictionItemOrm] = []
            for pred in predictionMultiOut.result:
                prediction_item = src.orm.prediction_item.PredictionItemOrm(
                    id=uuid.uuid4(),
                    prediction_id=prediction_inst.id,
                    prediction_result=pred.ranking[0].value,
                    prediction_result_percentage=pred.ranking[0].probability,
                    file_name=pred.filename,
                )
                prediction_items.append(prediction_item)

            session.add_all(prediction_items)

            session.commit()
        except Exception as e:
            print("🚀 ~ file: post__multi.py:91 ~ e:", e)
            session.rollback()
        finally:
            session.close()

    return predictionMultiOut


@router.get("/file/{filename}")
def get_uploaded_image(filename: str):
    filepath = f"assets/uploads/{filename}"
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return fastapi.responses.FileResponse(filepath, media_type="image/jpeg")

    return {}
