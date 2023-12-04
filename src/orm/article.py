"""
halo
"""

import typing
import time

import uuid
import sqlalchemy.orm


import src.orm.base_orm
import src.schema.base_schema


class ArticleOrm(src.orm.base_orm.BaseOrm):
    __tablename__ = "article"

    id = sqlalchemy.Column(
        sqlalchemy.CHAR(36),
        nullable=False,
        primary_key=True,
    )

    title = sqlalchemy.Column(
        sqlalchemy.String(255),
        nullable=False,
    )

    cover_url = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
    )

    description = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
    )

    article_url = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
    )

    created_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=False,
        default=time.time,
    )

    updated_at = sqlalchemy.Column(
        sqlalchemy.Double,
        nullable=True,
        default=None,
        onupdate=time.time,
    )

    def __init__(
        self,
        id,
        title,
        cover_url,
        description,
        article_url,
        created_at,
        updated_at,
        **kwargs: typing.Any,
    ):
        super().__init__(**kwargs)

        self.id = id
        self.title = title
        self.cover_url = cover_url
        self.description = description
        self.article_url = article_url
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"ArticleModel{vars(self)}"


class ArticleSchema(src.schema.base_schema.BaseSchema):
    id: str
    title: str
    cover_url: str
    description: str
    article_url: str
    created_at: float
    updated_at: typing.Optional[float]

    class Config:
        # orm_mode = True
        from_attributes = True
