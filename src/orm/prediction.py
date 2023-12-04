import typing
import time

import uuid
import sqlalchemy


import src.orm.base_orm
import src.schema.base_schema


class PredictionOrm(src.orm.base_orm.BaseOrm):
    __tablename__ = "prediction"

    id = sqlalchemy.Column(
        sqlalchemy.Uuid,
        nullable=False,
        primary_key=True,
    )

    user_id = sqlalchemy.Column(
        sqlalchemy.CHAR(36),
        nullable=True,
        default=None,
    )

    model_name = sqlalchemy.Column(
        sqlalchemy.String(50),
        nullable=False,
    )

    user_feedback = sqlalchemy.Column(
        sqlalchemy.CHAR,
        nullable=True,
        default=None,
    )

    user_feedback_detail = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=True,
        default=None,
    )

    feedbacked_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    requested_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=False,
        default=time.time,
    )

    def __init__(
        self,
        id,
        user_id,
        model_name,
        user_feedback,
        user_feedback_detail,
        feedbacked_at,
        requested_at,
        **kwargs: typing.Any,
    ):
        super().__init__(**kwargs)

        self.id = id
        self.user_id = user_id
        self.model_name = model_name
        self.user_feedback = user_feedback
        self.user_feedback_detail = user_feedback_detail
        self.feedbacked_at = feedbacked_at
        self.requested_at = requested_at

    def __repr__(self):
        return f"PredictionRequestModel{vars(self)}"


class PredictionSchema(src.schema.base_schema.BaseSchema):
    id: uuid.UUID
    user_id: typing.Union[uuid.UUID, None]
    model_name: str
    user_feedback: typing.Union[str, None]
    user_feedback_value: typing.Union[str, None]
    feedbacked_at: typing.Optional[float]
    requested_at: float

    class Config:
        from_attributes = True
