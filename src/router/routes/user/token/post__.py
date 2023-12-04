import time
import typing


import bcrypt
import fastapi
import jwt


import src.config.credential
import src.config.environment
import src.schema.base_schema
import src.service.user_service


router = fastapi.APIRouter()


class __In_LoginViaPassword(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["password"]
    username: str
    password: str


class __In_LoginViaGoogle(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["google"]
    google_id: str


class __In_LoginViaLinkedin(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["linkedin"]
    linkedin_id: str


class __In_LoginViaGithub(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["github"]
    github_id: str


class __In_LoginViaFacebook(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["facebook"]
    facebook_id: str


class __In_LoginViaTwitter(src.schema.base_schema.BaseSchema):
    login_via: typing.Literal["twitter"]
    twitter_id: str


class __Out_Login(src.schema.base_schema.Response):
    token: typing.Optional[str] = None
    refresh_token: typing.Optional[str] = None


@router.post("/")
def login(
    body: typing.Union[
        __In_LoginViaPassword,
        __In_LoginViaGoogle,
        __In_LoginViaLinkedin,
        __In_LoginViaGithub,
        __In_LoginViaFacebook,
        __In_LoginViaTwitter,
    ],
):
    match str(type(body)):
        case str(__In_LoginViaPassword):
            is_success, user_inst, error = src.service.user_service.find_user_by_username(body.username)

            if error != None:
                return __Out_Login(
                    message=f"server error {error.args}",
                    code=-1,
                    token=None,
                    refresh_token=None,
                )

            if user_inst is None:
                return __Out_Login(
                    message="user tidak ditemukan",
                    code=1,
                    token=None,
                    refresh_token=None,
                )

            is_pw_match = bcrypt.checkpw(password=body.password.encode(), hashed_password=user_inst.password.encode())
            if is_pw_match == False:
                return __Out_Login(
                    message="password salah",
                    code=2,
                    token=None,
                    refresh_token=None,
                )

            token_exp = int(time.time() + src.config.environment.APP_JWT_EXP_DAYS * 86400)
            token: str
            try:
                payload = src.config.credential.PayloadStructure(
                    username=body.username,
                    exp=token_exp,
                    iat=int(time.time()),
                    type=1,
                ).model_dump()
                filter_payload = {k: v for k, v in payload.items() if v is not None}
                token = jwt.encode(
                    payload=filter_payload,
                    key=src.config.environment.APP_JWT_SECRET,
                )
            except Exception as e:
                print("🚀 ~ file: post__.py:110 ~ e:", e)
                return __Out_Login(
                    message=f"server bermasalah: {e.args}",
                    code=3,
                    token=None,
                    refresh_token=None,
                )

            refresh_token_exp = int(time.time() + src.config.environment.APP_REFRESH_JWT_EXP_DAYS + 86400)
            refresh_token: str
            try:
                payload = src.config.credential.PayloadStructure(
                    username=body.username,
                    type=2,
                    exp=refresh_token_exp,
                    iat=int(time.time()),
                ).model_dump()
                filter_payload = {k: v for k, v in payload.items() if v is not None}
                refresh_token = jwt.encode(
                    payload=filter_payload,
                    key=src.config.environment.APP_REFRESH_JWT_SECRET,
                )
            except Exception as e:
                print("🚀 ~ file: post__.py:116 ~ e:", e)
                return __Out_Login(
                    message=f"server bermasalah: {e.args}",
                    code=3,
                    token=None,
                    refresh_token=None,
                )

            return __Out_Login(
                message="login sukses",
                code=0,
                token=token,
                refresh_token=refresh_token,
            )

        case str(__In_LoginViaGoogle), str(__In_LoginViaLinkedin), str(__In_LoginViaGithub), str(__In_LoginViaFacebook), str(__In_LoginViaTwitter), _:
            return __Out_Login(
                message="login is not implemented yet",
                code=2,
                token=None,
                refresh_token=None,
            )
