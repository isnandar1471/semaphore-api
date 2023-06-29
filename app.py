import logging
import os
import shutil
import subprocess
from datetime import datetime, date
from platform import python_version

import fastapi
import numpy
import tensorflow
from fastapi.responses import JSONResponse, FileResponse
from keras import __version__ as keras_version
from keras import models
from tensorflow import __version__ as tensorflow_version

# from app.db.models import UserAnswer
# from app.api import api


today: date = date.today()

logger = logging.getLogger(__name__)

formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")

file_handler = logging.FileHandler(f"logs/{today}.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

app = fastapi.FastAPI()


@app.get(
    "/",
)
def get_backend_information(request: fastapi.Request) -> JSONResponse:
    """
    Get backend information
    """

    logger.info(f"{request.client.host} accessing {request.url.path}")

    current_commit: subprocess.CompletedProcess = subprocess.run(
        ["git", "describe", "--always"], capture_output=True
    )
    current_commit: str = current_commit.stdout.decode().strip()

    system_spec: subprocess.CompletedProcess = subprocess.run(
        ["cat", "/etc/os-release"], capture_output=True
    )
    system_spec: str = system_spec.stdout.decode().strip()

    response = {
        "current_commit": current_commit,
        "system_spec": system_spec,
        "fastapi_version": fastapi.__version__,
        "python_version": python_version(),
        "np_version": numpy.__version__,
        "tf_version": tensorflow_version,
        "keras_version": keras_version,
    }
    return JSONResponse(response)


@app.post(
    "/semaphores/predict",
)
def predict_image(request: fastapi.Request, file: fastapi.UploadFile) -> JSONResponse:
    """
    Prediksi gambar
    """

    logger.info(f"{request.client.host} accessing {request.url.path}")

    current_datetime: datetime = datetime.now()
    formated_datetime: str = current_datetime.strftime("%Y-%m-%d %H-%M-%S %f")

    filepath = f"assets/uploads/{formated_datetime}.jpg"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        logger.info(f"'{filepath}' created")

    classes = [chr(x) for x in range(65, 90 + 1)]

    # TODO: mengubah menjadi pencarian berdasarkan regex agar lebih mudah
    model = models.load_model(
        "assets/models/kagglenotebook_mdl-vgg16_2023-06-23@18-11-41.hdf5"
    )

    test_img = tensorflow.keras.preprocessing.image.load_img(
        filepath, target_size=(256, 128)
    )
    test_img = tensorflow.keras.preprocessing.image.img_to_array(test_img)
    test_img /= 255.0

    x = test_img[numpy.newaxis, ...]

    result: numpy.ndarray = model.predict(x)
    prediction_probabilities = tensorflow.math.top_k(result, k=3)

    top_k_scores: numpy.ndarray = prediction_probabilities.values.numpy()
    dict_class_entries: numpy.ndarray = prediction_probabilities.indices.numpy()

    top_k_scores.sort(0)
    dict_class_entries.sort(0)

    ranking: dict = {}
    for idx, val in numpy.ndenumerate(top_k_scores):
        ranking[idx[1] + 1] = {
            "value": classes[dict_class_entries[idx]],
            "probability": float(val),
        }

    return JSONResponse(
        {
            "ranking": ranking,
        },
    )


@app.get("/assets/uploads/{filename}")
def get_uploaded_image(filename: str) -> FileResponse:
    filepath: str = f"assets/uploads/{filename}"
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return FileResponse(filepath, media_type="image/jpeg")

    return {}
