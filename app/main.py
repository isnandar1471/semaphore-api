import os

# os.system("conda activate py3_10_11")

from fastapi import FastAPI, HTTPException, UploadFile, File
from starlette.responses import Response
from tensorflow.keras.models import load_model
from numpy import argmax

from platform import python_version
from numpy import __version__ as np_version
from tensorflow import __version__ as tf_version
from tensorflow.keras import __version__ as keras_version
from matplotlib import __version__ as mtlp_version
import matplotlib.pyplot as plt

from app.db.models import UserAnswer
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Fast API in Python",
        "python_version": python_version(),
        "np_version": np_version,
        "tf_version": tf_version,
        "keras_version": keras_version,
        "mtlp_version": mtlp_version,
    }


@app.post("/semaphores/predict")
def predict_image(file: UploadFile | None = None):
    # if file == None:
    #     return {"msg": "file tidak ada"}

    # return {"msg": "file ada", "filename": file.filename}

    classes = [chr(x) for x in range(65, 90 + 1)]

    with open(
        "app/asset/2023-05-28@15-37-33__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.hdf5",
        # "app/asset/2023-05-29@09-21-32__epoch@{epoch_02d}__loss@{loss}__accuracy@{accuracy}__val_loss@{val_loss}__val_accuracy@{val_accuracy_.2f}__finish.h5",
        "rb",
    ) as f:
        print("passed")
        model = load_model(f)

    result = model.predict("app/asset/kelas1_5.png")
    predicted_value = argmax(result)

    return {
        # "hasil": classes[predicted_value],
        "classes": classes,
        "predicted_value": predicted_value,
    }


# @app.get("/user")
# def read_user():
#     return api.read_user()


# @app.get("/question/{position}", status_code=200)
# def read_questions(position: int, response: Response):
#     question = api.read_questions(position)

#     if not question:
#         raise HTTPException(status_code=400, detail="Error")

#     return question


# @app.get("/alternatives/{question_id}")
# def read_alternatives(question_id: int):
#     return api.read_alternatives(question_id)


# @app.post("/answer", status_code=201)
# def create_answer(payload: UserAnswer):
#     payload = payload.dict()

#     return api.create_answer(payload)


# @app.get("/result/{user_id}")
# def read_result(user_id: int):
#     return api.read_result(user_id)
