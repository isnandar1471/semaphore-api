import time
import shutil

# import os
import numpy

# import matplotlib.pyplot as plt
import tensorflow
from starlette.responses import Response
from platform import python_version
import numpy
from numpy import __version__ as np_version
from matplotlib import __version__ as mtlp_version
from fastapi import FastAPI, HTTPException, UploadFile, File

# from app.db.models import UserAnswer
# from app.api import api

app = FastAPI()


@app.get(
    "/",
)
def root():
    return {
        "message": "Fast API in Python",
        "python_version": python_version(),
        "np_version": np_version,
        "tf_version": tensorflow.__version__,
        "keras_version": tensorflow.keras.__version__,
        "mtlp_version": mtlp_version,
    }


@app.post(
    "/semaphores/predict",
)
def predict_image(file: UploadFile | None = None):
    if file == None:
        return HTTPException(status_code=400, detail={"msg": "file tidak ada"})

    now = time.time()
    filepath = f"app/asset/upload/{now}.jpg"

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # return {"msg": "file ada", "filename": file.filename}

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
        # "classes": classes,
        "predicted_value": classes[predicted_value],
    }
