"""create-article

Revision ID: 9e467fad46f6
Revises:
Create Date: 2023-11-19 10:14:28.156150

"""

import typing

import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "9e467fad46f6"
down_revision: typing.Union[str, None] = None
branch_labels: typing.Union[str, typing.Sequence[str], None] = None
depends_on: typing.Union[str, typing.Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "article",
        sqlalchemy.Column("id", sqlalchemy.CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("title", sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column("cover_url", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("description", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("article_url", sqlalchemy.Text, nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.Double, nullable=False),
        sqlalchemy.Column("updated_at", sqlalchemy.Double, nullable=True, default=None),
    )


def downgrade() -> None:
    alembic.op.drop_table("article")
