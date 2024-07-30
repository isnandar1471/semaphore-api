"""update-prediction-table

Revision ID: 9a4454cb531c
Revises: 185eb15f1714
Create Date: 2024-07-30 10:38:24.675374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from alembic.op import add_column, drop_column
from sqlalchemy import Column, DOUBLE

# revision identifiers, used by Alembic.
revision: str = '9a4454cb531c'
down_revision: Union[str, None] = '185eb15f1714'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    add_column('prediction',
        Column('feedbacked_at', DOUBLE, nullable=True, default=None)
    )


def downgrade() -> None:
    drop_column('prediction', 'feedbacked_at')
