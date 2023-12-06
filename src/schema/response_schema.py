import typing


import src.schema.base_schema


class Article(src.schema.base_schema.BaseSchema):
    id: str
    title: str
    cover_url: str
    description: str
    article_url: str
    created_at: int
    updated_at: typing.Union[int, None] = None


class BackEndInformation(src.schema.base_schema.BaseSchema):
    current_commit: str
    system_spec: str
    fastapi_version: str
    python_version: str
    numpy_version: str
    tensorflow_version: str
    keras_version: str


class Prediction(src.schema.base_schema.BaseSchema):
    filename: str
    ranking: list[src.schema.base_schema.Ranking] = []


class PredictionMulti(src.schema.base_schema.BaseSchema):
    result: list[Prediction] = []
    prediction_id: typing.Union[str, None] = None
