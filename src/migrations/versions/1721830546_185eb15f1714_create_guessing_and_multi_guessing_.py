"""create guessing and multi-guessing tables

Revision ID: 185eb15f1714
Revises: 429ec8f730b0
Create Date: 2024-07-24 21:15:46.829648

"""
from typing import Sequence, Union

import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "185eb15f1714"
down_revision: Union[str, None] = "2778cf46c3f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "guessing",
        sqlalchemy.Column("id", sqlalchemy.CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("user_id", sqlalchemy.CHAR(36), nullable=True, default=None),
        sqlalchemy.Column("filepath", sqlalchemy.VARCHAR(255), nullable=False),
        sqlalchemy.Column("actual_value", sqlalchemy.CHAR(1), nullable=False),
        sqlalchemy.Column("created_at", sqlalchemy.DOUBLE, nullable=False),
        sqlalchemy.Column("predicted_at", sqlalchemy.DOUBLE, nullable=True, default=None),
        sqlalchemy.Column("predicted_value", sqlalchemy.CHAR(1), nullable=True, default=None),
        sqlalchemy.Column("updated_at", sqlalchemy.DOUBLE, nullable=True, default=None),
    )

    alembic.op.create_table(
        "multi_guessing",
        sqlalchemy.Column("id", sqlalchemy.CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        sqlalchemy.Column("user_id", sqlalchemy.CHAR(36), nullable=True, default=None),
        sqlalchemy.Column("created_at", sqlalchemy.DOUBLE, nullable=False),
        sqlalchemy.Column("predicted_at", sqlalchemy.DOUBLE, nullable=True, default=None),
        sqlalchemy.Column("actual_value", sqlalchemy.TEXT, nullable=False),
        sqlalchemy.Column("predicted_value", sqlalchemy.TEXT, nullable=True, default=None),
        sqlalchemy.Column("updated_at", sqlalchemy.DOUBLE, nullable=True, default=None),
    )


def downgrade() -> None:
    alembic.op.drop_table("multi_guessing")

    alembic.op.drop_table("guessing")
