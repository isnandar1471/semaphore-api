"""create_prediction

Revision ID: 2778cf46c3f6
Revises: f9dfe6ab786c
Create Date: 2023-11-30 08:40:07.381576

"""

import typing

import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "2778cf46c3f6"
down_revision: typing.Union[str, None] = "f9dfe6ab786c"
branch_labels: typing.Union[str, typing.Sequence[str], None] = None
depends_on: typing.Union[str, typing.Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "prediction",  # utama
        sqlalchemy.Column("id", sqlalchemy.CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("user_id", sqlalchemy.CHAR(36), nullable=True, default=None),
        sqlalchemy.Column("model_name", sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column("user_feedback", sqlalchemy.CHAR, nullable=True, default=None),
        sqlalchemy.Column("user_feedback_detail", sqlalchemy.String(255), nullable=True, default=None),
        sqlalchemy.Column("requested_at", sqlalchemy.Double, nullable=False),
    )


def downgrade() -> None:
    alembic.op.drop_table("prediction")
    pass
