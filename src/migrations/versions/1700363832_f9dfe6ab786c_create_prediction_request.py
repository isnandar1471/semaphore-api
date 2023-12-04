"""create-prediction_request

Revision ID: f9dfe6ab786c
Revises: 24ed734b73ee
Create Date: 2023-11-19 10:17:12.864852

"""

import typing

import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "f9dfe6ab786c"
down_revision: typing.Union[str, None] = "24ed734b73ee"
branch_labels: typing.Union[str, typing.Sequence[str], None] = None
depends_on: typing.Union[str, typing.Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "prediction_request",
        sqlalchemy.Column("id", sqlalchemy.CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("prediction_result", sqlalchemy.CHAR, nullable=False),
        sqlalchemy.Column("prediction_result_percentage", sqlalchemy.Float, nullable=False),
        sqlalchemy.Column("model_name", sqlalchemy.String(50), nullable=False),
        sqlalchemy.Column("file_name", sqlalchemy.String(50), nullable=False, unique=True),
        sqlalchemy.Column("user_id", sqlalchemy.Uuid, nullable=True, default=None),
        sqlalchemy.Column("requested_at", sqlalchemy.Double, nullable=False),
        sqlalchemy.Column("user_feedback_value", sqlalchemy.CHAR, nullable=True, default=None),
        sqlalchemy.Column("feedbacked_at", sqlalchemy.Double, nullable=True, default=None),
    )


def downgrade() -> None:
    alembic.op.drop_table("prediction_request")
