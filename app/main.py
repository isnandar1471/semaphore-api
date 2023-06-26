import datetime
import fastapi
import logging
import matplotlib
import numpy
import numpy
import os
import platform
import shutil
import starlette
import tensorflow
import time
import uvicorn
import subprocess

# from app.db.models import UserAnswer
# from app.api import api


today = datetime.date.today()

logging.basicConfig(
    filename="log/{today}.log",
    format="%(asctime)s %(message)s",
    filemode="w",
)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = fastapi.FastAPI()


@app.get(
    "/",
)
def get_backend_information(request: fastapi.Request):
    """
    Get backend information
    """

    logger.info(f"{request.client.host} accessing /")
    return {
        "git describe --always": subprocess.check_output(
            ["git", "describe", "--always"]
        ),
        "message": "Fast API in Python",
        "fastapi_version": fastapi.__version__,
        "python_version": platform.python_version(),
        "np_version": numpy.__version__,
        "tf_version": tensorflow.__version__,
        "keras_version": tensorflow.keras.__version__,
        "mtlp_version": matplotlib.__version__,
    }


@app.post(
    "/semaphores/predict",
)
def predict_image(request: fastapi.Request, file: fastapi.UploadFile | None = None):
    logger.info(f"{request.client.host} accessing /semaphores/predict")
    if file == None:
        return {"msg": "file tidak ada"}

    now = time.time()
    filepath = f"app/asset/upload/{now}.jpg"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(f"{filepath} created")

    classes = [chr(x) for x in range(65, 90 + 1)]

    # TODO: mengubah menjadi pencarian berdasarkan regex agar lebih mudah
    model = tensorflow.keras.models.load_model(
        "app/asset/kagglenotebook_mdl-vgg16_2023-06-23@18-11-41.hdf5"
    )

    test_img = tensorflow.keras.preprocessing.image.load_img(
        filepath, target_size=(256, 128)
    )
    test_img = tensorflow.keras.preprocessing.image.img_to_array(test_img)
    test_img /= 255.0

    x = test_img[numpy.newaxis, ...]
    x = tensorflow.keras.applications.vgg16.preprocess_input(x)

    # mengubah prediksi menjadi top-k
    result = model.predict(x)
    predicted_value = numpy.argmax(result)

    return {
        "predicted_value": classes[predicted_value],
    }


@app.get("/asset/{filename}")
def get_uploaded_image_by_filename(filename: str):
    return starlette.responses.FileResponse(
        f"app/asset/upload/{filename}", media_type="image/jpeg"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
