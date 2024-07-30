"""change prediction_request to prediction_item

Revision ID: 97f31be4ee36
Revises: 9a4454cb531c
Create Date: 2024-07-30 12:39:52.237476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from alembic.op import drop_table, create_table, create_foreign_key, drop_constraint
from sqlalchemy import Column, CHAR, FLOAT, DOUBLE, VARCHAR

# revision identifiers, used by Alembic.
revision: str = '97f31be4ee36'
down_revision: Union[str, None] = '9a4454cb531c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    drop_table('prediction_request')

    create_table('prediction_item',
        Column('id', CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        Column('prediction_id', CHAR(36), nullable=False, ),
        Column('prediction_result', CHAR(1), nullable=False, ),
        Column('prediction_result_percentage', FLOAT, nullable=False, ),
        Column('file_name', VARCHAR(255), nullable=False, ),
    )

    create_foreign_key(
        'FK_prediction_id',
        'prediction_item',
        'prediction',
        ['prediction_id'],
        ['id'],
        onupdate='CASCADE',
        ondelete='RESTRICT',
    )

def downgrade() -> None:
    drop_constraint('FK_prediction_id', 'prediction_item', 'foreignkey')

    drop_table('prediction_item')

    create_table('prediction_request',
        Column("id", CHAR(36), nullable=False, primary_key=True, comment="UUID unit"),
        Column("prediction_result", CHAR(1), nullable=False),
        Column("prediction_result_percentage", FLOAT, nullable=False),
        Column("model_name", VARCHAR(50), nullable=False),
        Column("file_name", VARCHAR(50), nullable=False, unique=True),
        Column("user_id", CHAR(36), nullable=True, default=None),
        Column("requested_at", DOUBLE, nullable=False),
        Column("user_feedback_value", CHAR(1), nullable=True, default=None),
        Column("feedbacked_at", DOUBLE, nullable=True, default=None),
    )
