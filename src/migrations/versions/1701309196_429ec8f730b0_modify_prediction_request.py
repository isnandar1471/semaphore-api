"""modify_prediction_request

Revision ID: 429ec8f730b0
Revises: 2778cf46c3f6
Create Date: 2023-11-30 08:53:16.705689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '429ec8f730b0'
down_revision: Union[str, None] = '2778cf46c3f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
