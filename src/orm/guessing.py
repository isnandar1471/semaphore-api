import time
import typing

import sqlalchemy
import uuid

import src.orm.base_orm
import src.schema.base_schema


class GuessingOrm(src.orm.base_orm.BaseOrm):
    __tablename__ = "guessing"

    id = sqlalchemy.Column(
        sqlalchemy.CHAR(36),
        nullable=False,
        primary_key=True,
        default=uuid.uuid4,
    )

    user_id = sqlalchemy.Column(
        sqlalchemy.CHAR(36),
        nullable=True,
        default=None,
    )

    filepath = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=False,
    )

    actual_value = sqlalchemy.Column(
        sqlalchemy.CHAR(1),
        nullable=False,
    )

    created_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=False,
        default=time.time,
    )

    predicted_value = sqlalchemy.Column(
        sqlalchemy.CHAR(1),
        nullable=True,
        default=None,
    )

    predicted_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    updated_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    def __init__(
        self,
        filepath: str,
        actual_value: str,
        id: typing.Optional[typing.Union[str, uuid.UUID]] = None,
        user_id: typing.Optional[typing.Union[str, uuid.UUID]] = None,
        created_at: typing.Optional[float] = None,
        predicted_value: typing.Optional[str] = None,
        predicted_at: typing.Optional[float] = None,
        updated_at: typing.Optional[float] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(**kwargs)

        self.id = str(id if id != None else uuid.uuid4())
        self.user_id = str(user_id) if user_id != None else None
        self.filepath = filepath
        self.actual_value = actual_value
        self.created_at = created_at if created_at != None else time.time()
        self.predicted_value = predicted_value
        self.predicted_at = predicted_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{vars(self)}"


class GuessingSchema(src.schema.base_schema.BaseSchema):
    id: str
    user_id: typing.Union[str, None] = None
    filepath: str
    actual_value: str
    created_at: float
    predicted_value: typing.Union[str, None] = None
    predicted_at: typing.Union[float, None] = None
    updated_at: typing.Union[float, None] = None

    class Config:
        from_attributes = True
