import os


import numpy
import tensorflow
import keras.utils
import keras.models
import keras.engine.functional


import src.config.environment
import src.config.constant
import src.schema.base_schema
import src.schema.response_schema


model: keras.engine.functional.Functional = keras.models.load_model(src.config.environment.APP_MODEL_HDF5_PATH)


def predict_image(filepath: str):
    test_img = keras.utils.load_img(filepath, target_size=(256, 128))
    test_img = keras.utils.img_to_array(test_img)
    test_img /= 255.0

    x = test_img[numpy.newaxis, ...]

    result: numpy.ndarray = model.predict(x)
    prediction_probabilities = tensorflow.math.top_k(result, k=3)

    top_k_scores: numpy.ndarray = prediction_probabilities.values.numpy()
    dict_class_entries: numpy.ndarray = prediction_probabilities.indices.numpy()

    top_k_scores.sort(0)
    dict_class_entries.sort(0)

    predictionOut = src.schema.response_schema.Prediction(filename=os.path.basename(filepath))
    for idx, val in numpy.ndenumerate(top_k_scores):
        predictionOut.ranking.append(
            src.schema.base_schema.Ranking(
                rank=idx[1] + 1,
                value=src.config.constant.CLASSES[dict_class_entries[idx]],
                probability=float(val),
            )
        )

    return predictionOut


def predict_multi_image(filepaths: list[str]):
    predictionMultiOut = src.schema.response_schema.PredictionMulti()
    for filepath in filepaths:
        predictionOut = predict_image(filepath)

        predictionMultiOut.result.append(predictionOut)

    return predictionMultiOut
