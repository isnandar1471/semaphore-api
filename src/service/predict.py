import os


import keras
import keras.src.engine.functional
import numpy
import tensorflow


from ..schema import base_schema, response_schema
from ..config import constant


model: keras.src.engine.functional.Functional = keras.models.load_model(os.getenv("APP_MODEL_HDF5_PATH"))


def predict_image(filepath: str):
    test_img = keras.preprocessing.image.load_img(filepath, target_size=(256, 128))
    test_img = keras.preprocessing.image.img_to_array(test_img)
    test_img /= 255.0

    x = test_img[numpy.newaxis, ...]

    result: numpy.ndarray = model.predict(x)
    prediction_probabilities = tensorflow.math.top_k(result, k=3)

    top_k_scores: numpy.ndarray = prediction_probabilities.values.numpy()
    dict_class_entries: numpy.ndarray = prediction_probabilities.indices.numpy()

    top_k_scores.sort(0)
    dict_class_entries.sort(0)

    base_url = os.getenv("APP_HTTP_URL_PUBLIC", "http://127.0.0.1")
    predictionOut = response_schema.PredictionOut(image_url=f"{base_url}/a/{filepath}")
    for idx, val in numpy.ndenumerate(top_k_scores):
        predictionOut.ranking.append(
            base_schema.Ranking(
                rank=idx[1] + 1,
                value=constant.CLASSES[dict_class_entries[idx]],
                probability=float(val),
            )
        )

    return predictionOut


def predict_multi_image(filepaths: list[str]):
    predictionMultiOut = response_schema.PredictionMultiOut()
    for filepath in filepaths:
        predictionOut = predict_image(filepath)

        predictionMultiOut.result.append(predictionOut)

    return predictionMultiOut
