import typing
import time

import uuid
import sqlalchemy


import src.orm.base_orm
import src.schema.base_schema


class PredictionItemOrm(src.orm.base_orm.BaseOrm):
    __tablename__ = "prediction_item"

    id = sqlalchemy.Column(
        sqlalchemy.Uuid,
        nullable=False,
        primary_key=True,
    )

    prediction_id = sqlalchemy.Column(
        sqlalchemy.Uuid,
        nullable=False,
    )

    prediction_result = sqlalchemy.Column(
        sqlalchemy.CHAR,
        nullable=False,
    )

    prediction_result_percentage = sqlalchemy.Column(
        sqlalchemy.Float,
        nullable=False,
    )

    file_name = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=False,
        unique=True,
    )

    def __init__(
        self,
        id,
        prediction_id,
        prediction_result,
        prediction_result_percentage,
        file_name,
        **kwargs: typing.Any,
    ):
        super().__init__(**kwargs)

        self.id = id
        self.prediction_id = prediction_id
        self.prediction_result = prediction_result
        self.prediction_result_percentage = prediction_result_percentage
        self.file_name = file_name

    def __repr__(self):
        return f"PredictionRequestModel{vars(self)}"


class PredictionItemSchema(src.schema.base_schema.BaseSchema):
    id: uuid.UUID
    prediction_result: str
    prediction_result_percentage: float
    file_name: str

    class Config:
        from_attributes = True
