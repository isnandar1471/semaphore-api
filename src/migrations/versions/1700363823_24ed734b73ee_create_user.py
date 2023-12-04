"""create-user

Revision ID: 24ed734b73ee
Revises: 9e467fad46f6
Create Date: 2023-11-19 10:17:03.243297

"""

import typing

import alembic
import sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "24ed734b73ee"
down_revision: typing.Union[str, None] = "9e467fad46f6"
branch_labels: typing.Union[str, typing.Sequence[str], None] = None
depends_on: typing.Union[str, typing.Sequence[str], None] = None


def upgrade() -> None:
    alembic.op.create_table(
        "user",
        sqlalchemy.Column(name="id", type_=sqlalchemy.CHAR(36), nullable=False, primary_key=True),
        sqlalchemy.Column(name="username", type_=sqlalchemy.String(255), nullable=False, unique=True),
        sqlalchemy.Column(name="email", type_=sqlalchemy.String(255), nullable=False, unique=True),
        sqlalchemy.Column(name="registered_at", type_=sqlalchemy.Double, nullable=False),
        sqlalchemy.Column(name="email_verification_key", type_=sqlalchemy.String(255), nullable=True, default=None, comment="Base64 from string JSON of EmailVerificationKey object"),
        sqlalchemy.Column(name="is_email_verified", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="email_verified_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="can_login_via_password", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="can_login_via_google", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="can_login_via_linkedin", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="can_login_via_github", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="can_login_via_facebook", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="can_login_via_twitter", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="password", type_=sqlalchemy.String(255), nullable=True, default=None),
        sqlalchemy.Column(name="google_id", type_=sqlalchemy.String(255), nullable=True, default=None, unique=True),
        sqlalchemy.Column(name="google_connected_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="linkedin_id", type_=sqlalchemy.String(255), nullable=True, default=None, unique=True),
        sqlalchemy.Column(name="linkedin_connected_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="github_id", type_=sqlalchemy.String(255), nullable=True, default=None, unique=True),
        sqlalchemy.Column(name="github_connected_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="facebook_id", type_=sqlalchemy.String(255), nullable=True, default=None, unique=True),
        sqlalchemy.Column(name="facebook_connected_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="twitter_id", type_=sqlalchemy.String(255), nullable=True, default=None, unique=True),
        sqlalchemy.Column(name="twitter_connected_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="is_mastering_semaphore", type_=sqlalchemy.Boolean, nullable=False, default=False),
        sqlalchemy.Column(name="proof_mastering_semaphore_filename", type_=sqlalchemy.String(255), nullable=True, default=None),
        sqlalchemy.Column(name="semaphore_test_id", type_=sqlalchemy.Integer, nullable=True, default=None),
        sqlalchemy.Column(name="mastering_semaphore_verified_at", type_=sqlalchemy.Double, nullable=True, default=None),
        sqlalchemy.Column(name="last_updated_at", type_=sqlalchemy.Double, nullable=True, default=None),
    )


def downgrade() -> None:
    alembic.op.drop_table("user")
