from . import base_schema


class ArticleOut(base_schema.BaseSchema):
    id: str
    title: str
    cover_url: str
    description: str
    article_url: str
    created_at: int
    updated_at: int | None


class BackendInformationOut(base_schema.BaseSchema):
    current_commit: str
    system_spec: str
    fastapi_version: str
    python_version: str
    numpy_version: str
    tensorflow_version: str
    keras_version: str


class PredictionOut(base_schema.BaseSchema):
    image_url: str
    ranking: list[base_schema.Ranking] = []


class PredictionMultiOut(base_schema.BaseSchema):
    result: list[PredictionOut] = []
