import typing


import sqlalchemy


from . import base_model


class ArticleModel(base_model.BaseModel):
    __tablename__ = "article"

    id = sqlalchemy.Column(
        sqlalchemy.Uuid,
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
        sqlalchemy.Integer,
        nullable=False,
        server_default=sqlalchemy.text("unix_timestamp()"),
    )

    updated_at = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=True,
        server_default=sqlalchemy.text("null"),
        server_onupdate=sqlalchemy.text("unix_timestamp()"),
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
        return f"Article(id={self.id!r}, title={self.title!r}, cover_url={self.cover_url!r}, description={self.description!r}, article_url={self.article_url!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r})"
