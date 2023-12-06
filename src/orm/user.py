import typing
import time
import uuid
import base64

import uuid
import sqlalchemy


import src.orm.base_orm
import src.config.credential
import src.schema.base_schema


class UserOrm(src.orm.base_orm.BaseOrm):
    __tablename__ = "user"

    id = sqlalchemy.Column(
        type_=sqlalchemy.CHAR(36),
        nullable=False,
        primary_key=True,
        default=uuid.uuid4,
    )

    username = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=False,
        unique=True,
    )

    email = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=False,
        unique=True,
    )

    registered_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=False,
        default=time.time,
    )

    email_verification_key = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
    )

    is_email_verified = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    email_verified_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    can_login_via_password = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    can_login_via_google = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    can_login_via_linkedin = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    can_login_via_github = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    can_login_via_facebook = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    can_login_via_twitter = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    password = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
    )

    google_id = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
        unique=True,
    )

    google_connected_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    linkedin_id = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
        unique=True,
    )

    linkedin_connected_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    github_id = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
        unique=True,
    )

    github_connected_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    facebook_id = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
        unique=True,
    )

    facebook_connected_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    twitter_id = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
        unique=True,
    )

    twitter_connected_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    is_mastering_semaphore = sqlalchemy.Column(
        type_=sqlalchemy.Boolean,
        nullable=False,
        default=False,
    )

    proof_mastering_semaphore_filename = sqlalchemy.Column(
        type_=sqlalchemy.String(255),
        nullable=True,
        default=None,
    )

    semaphore_test_id = sqlalchemy.Column(
        type_=sqlalchemy.Integer,
        nullable=True,
        default=None,
    )

    mastering_semaphore_verified_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
    )

    last_updated_at = sqlalchemy.Column(
        type_=sqlalchemy.Double,
        nullable=True,
        default=None,
        onupdate=time.time,
    )

    def __init__(
        self,
        username,
        email,
        id: typing.Optional[uuid.UUID] = None,
        registered_at: typing.Optional[float] = None,
        email_verification_key: typing.Optional[str] = None,
        is_email_verified: bool = False,
        email_verified_at: typing.Optional[float] = None,
        can_login_via_password: bool = False,
        can_login_via_google: bool = False,
        can_login_via_linkedin: bool = False,
        can_login_via_github: bool = False,
        can_login_via_facebook: bool = False,
        can_login_via_twitter: bool = False,
        password: typing.Optional[str] = None,
        google_id: typing.Optional[str] = None,
        google_connected_at: typing.Optional[float] = None,
        linkedin_id: typing.Optional[str] = None,
        linkedin_connected_at: typing.Optional[float] = None,
        github_id: typing.Optional[str] = None,
        github_connected_at: typing.Optional[float] = None,
        facebook_id: typing.Optional[str] = None,
        facebook_connected_at: typing.Optional[float] = None,
        twitter_id: typing.Optional[str] = None,
        twitter_connected_at: typing.Optional[float] = None,
        is_mastering_semaphore: bool = False,
        proof_mastering_semaphore_filename: typing.Optional[str] = None,
        semaphore_test_id: typing.Optional[int] = None,
        mastering_semaphore_verified_at: typing.Optional[float] = None,
        last_updated_at: typing.Optional[float] = None,
        **kwargs: typing.Any,
    ):
        super().__init__(**kwargs)

        self.id = str(id if id is not None else uuid.uuid4())
        self.username = username
        self.email = email
        self.registered_at = registered_at if registered_at is not None else time.time()
        self.email_verification_key = email_verification_key if email_verification_key is not None else base64.b64encode(src.config.credential.EmailVerificationKey(uuid4=uuid.uuid4(), version=1, generated_at=time.time()).model_dump_json().encode()).decode()
        self.is_email_verified = is_email_verified
        self.email_verified_at = email_verified_at
        self.can_login_via_password = can_login_via_password
        self.can_login_via_google = can_login_via_google
        self.can_login_via_linkedin = can_login_via_linkedin
        self.can_login_via_github = can_login_via_github
        self.can_login_via_facebook = can_login_via_facebook
        self.can_login_via_twitter = can_login_via_twitter
        self.password = password
        self.google_id = google_id
        self.google_connected_at = google_connected_at
        self.linkedin_id = linkedin_id
        self.linkedin_connected_at = linkedin_connected_at
        self.github_id = github_id
        self.github_connected_at = github_connected_at
        self.facebook_id = facebook_id
        self.facebook_connected_at = facebook_connected_at
        self.twitter_id = twitter_id
        self.twitter_connected_at = twitter_connected_at
        self.is_mastering_semaphore = is_mastering_semaphore
        self.proof_mastering_semaphore_filename = proof_mastering_semaphore_filename
        self.semaphore_test_id = semaphore_test_id
        self.mastering_semaphore_verified_at = mastering_semaphore_verified_at
        self.last_updated_at = last_updated_at

    def __repr__(self) -> str:
        return f"UserModel{vars(self)}"


class UserSchema(src.schema.base_schema.BaseSchema):
    id: str
    username: str
    email: str
    registered_at: float
    email_verification_key: typing.Optional[str]
    is_email_verified: bool
    email_verified_at: typing.Optional[float]
    can_login_via_password: bool
    can_login_via_google: bool
    can_login_via_linkedin: bool
    can_login_via_github: bool
    can_login_via_facebook: bool
    can_login_via_twitter: bool
    password: typing.Optional[str]
    google_id: typing.Optional[str]
    google_connected_at: typing.Optional[float]
    linkedin_id: typing.Optional[str]
    linkedin_connected_at: typing.Optional[float]
    github_id: typing.Optional[str]
    github_connected_at: typing.Optional[float]
    facebook_id: typing.Optional[str]
    facebook_connected_at: typing.Optional[float]
    twitter_id: typing.Optional[str]
    twitter_connected_at: typing.Optional[float]
    is_mastering_semaphore: bool
    proof_mastering_semaphore_filename: typing.Optional[str]
    semaphore_test_id: typing.Optional[int]
    mastering_semaphore_verified_at: typing.Optional[float]
    last_updated_at: typing.Optional[float]

    class Config:
        from_attributes = True
