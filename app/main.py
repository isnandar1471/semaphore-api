import time
import shutil
import numpy
import os

import matplotlib
import tensorflow
import starlette
import platform
import numpy
import fastapi
import uvicorn

# from app.db.models import UserAnswer
# from app.api import api

app = fastapi.FastAPI()


@app.get(
    "/",
)
def root():
    return {
        "message": "Fast API in Python",
        "python_version": platform.python_version(),
        "np_version": numpy.__version__,
        "tf_version": tensorflow.__version__,
        "keras_version": tensorflow.keras.__version__,
        "mtlp_version": matplotlib.__version__,
    }


@app.post(
    "/semaphores/predict",
)
def predict_image(file: fastapi.UploadFile | None = None):
    if file == None:
        return {"msg": "file tidak ada"}

    now = time.time()
    filepath = f"app/asset/upload/{now}.jpg"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    classes = [chr(x) for x in range(65, 90 + 1)]

    model = tensorflow.keras.models.load_model(
        "app/asset/2023-05-28@15-37-33__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.hdf5"
    )

    test_img = tensorflow.keras.preprocessing.image.load_img(filepath)
    test_img = tensorflow.keras.preprocessing.image.img_to_array(test_img)
    test_img /= 255.0

    x = test_img[numpy.newaxis, ...]
    x = tensorflow.keras.applications.resnet50.preprocess_input(x)

    result = model.predict(x)
    predicted_value = numpy.argmax(result)

    return {
        "predicted_value": classes[predicted_value],
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
