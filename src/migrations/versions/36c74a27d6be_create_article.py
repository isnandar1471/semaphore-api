"""create-article

Revision ID: 36c74a27d6be
Revises:
Create Date: 2023-09-29 13:54:03.874846

"""
import typing


import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "36c74a27d6be"
down_revision: typing.Union[str, None] = None
branch_labels: typing.Union[str, typing.Sequence[str], None] = None
depends_on: typing.Union[str, typing.Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "article",
        sqlalchemy.Column("id", sqlalchemy.Uuid, nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("title", sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column("cover_url", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("article_url", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.Integer, nullable=False, comment="epoch second unit"),
        sqlalchemy.Column("updated_at", sqlalchemy.Integer, nullable=True, server_default=sqlalchemy.text("null"), comment="epoch second unit"),
    )


def downgrade() -> None:
    alembic.op.drop_table("article")
