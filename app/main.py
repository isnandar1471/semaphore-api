# tensorflow==2.12.0

import os

from fastapi import FastAPI, HTTPException, UploadFile, File
from starlette.responses import Response

from tensorflow.keras.models import load_model
import numpy as np
from numpy import argmax

from platform import python_version
from numpy import __version__ as np_version

from tensorflow import __version__ as tf_version
from tensorflow.keras import __version__ as keras_version
from matplotlib import __version__ as mtlp_version
import matplotlib.pyplot as plt
import cv2

from app.db.models import UserAnswer
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Fast API in Python",
        "python_version": python_version(),
        "np_version": np_version,
        # "tf_version": tf_version,
        # "keras_version": keras_version,
        "mtlp_version": mtlp_version,
    }


@app.post("/semaphores/predict")
def predict_image(file: UploadFile | None = None):
    # if file == None:
    #     return {"msg": "file tidak ada"}

    # return {"msg": "file ada", "filename": file.filename}

    classes = [chr(x) for x in range(65, 90 + 1)]

    # with open(
    #     "app/asset/2023-05-28@15-37-33__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.hdf5",
    #     # "app/asset/2023-05-29@09-21-32__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.h5",
    #     "rb",
    # ) as f:
    #     print("passed")
    model = load_model(
        "app/asset/2023-05-28@15-37-33__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.hdf5"
    )

    testfile_path = "app/asset/kelas1_5.png"
    test_img = cv2.imread(testfile_path)
    test_img = cv2.cvtColor(test_img, cv2.COLOR_RGB2BGR)

    test_img = np.asarray(test_img, dtype=float)
    test_img /= 255

    result = model.predict(np.expand_dims(test_img, 0))
    predicted_value = argmax(result)

    return {
        # "hasil": classes[predicted_value],
        "classes": classes,
        "predicted_value": classes[predicted_value],
    }
