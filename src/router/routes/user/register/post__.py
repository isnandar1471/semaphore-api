import base64
import time
import typing
import uuid


import bcrypt
import fastapi


import src.config.credential
import src.orm.user
import src.schema.base_schema
import src.service.user_service


class __Register(src.schema.base_schema.Response):
    pass


router = fastapi.APIRouter()


@router.post("/")
def register(
    username: typing.Annotated[
        str,
        fastapi.Form(
            max_length=255,
            pattern=r"^[a-zA-Z0-9]+$",
        ),
    ],
    email: typing.Annotated[
        str,
        fastapi.Form(
            max_length=255,
            pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        ),
    ],
    password: typing.Annotated[
        str,
        fastapi.Form(
            min_length=8,
            # pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()-_=+\[\]{}|;:,.<>?/])[A-Za-z\d!@#$%^&*()-_=+\[\]{}|;:,.<>?/]{8,}$",
            # pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d!@#$%^&*()-_=+\[\]{}|;:,.<>?/]{8,}$",
        ),
    ],
    # accept_language: __typing.Annotated[__typing.Union[str, None], fastapi.Header(alias="Accept-Language")] = '',
):
    is_success, user_inst, error = src.service.user_service.find_user_by_username(username)
    if error:
        return __Register(
            message=f"server mengalami masalah: {error.args}",
            code=1,
        )
    if user_inst:
        return __Register(
            message="username telah dipakai",
            code=2,
        )

    is_success, user_inst, error = src.service.user_service.find_user_by_email(email)
    if error:
        return __Register(
            message=f"server mengalami masalah: {error.args}",
            code=3,
        )

    if user_inst:
        return __Register(
            message="email telah dipakai",
            code=4,
        )

    user = src.orm.user.UserOrm(
        id=uuid.uuid4(),
        username=username,
        email=email,
        registered_at=time.time(),
        is_email_verified=False,
        can_login_via_password=True,
        can_login_via_google=False,
        can_login_via_linkedin=False,
        can_login_via_github=False,
        can_login_via_facebook=False,
        can_login_via_twitter=False,
        is_mastering_semaphore=False,
        password=bcrypt.hashpw(password=password.encode(), salt=bcrypt.gensalt()).decode(),
        email_verification_key=base64.b64encode(src.config.credential.EmailVerificationKey(uuid4=uuid.uuid4(), version=1, generated_at=time.time()).model_dump_json().encode()).decode(),
    )

    is_success, error = src.service.user_service.create_new_user(user)

    if is_success is False:
        return __Register(
            message=f"Server mengalami error: {error.args}",
            code=5,
        )

    return __Register(
        message="berhasil membuat user",
        code=0,
    )
