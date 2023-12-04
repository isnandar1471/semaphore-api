import typing


import fastapi


import src.service.user_service
import src.schema.base_schema

router = fastapi.APIRouter()


class __CheckUsernameAvailability(src.schema.base_schema.Response):
    is_available: typing.Optional[bool] = None


@router.post("/")
def check_username_availability(
    username: typing.Annotated[str, fastapi.Form()],
):
    user_inst, error = src.service.user_service.find_user_by_username(username)
    if error is not None:
        return __CheckUsernameAvailability(
            message=f"server mengalami masalah: {error.args}",
            code=1,
        )
    if user_inst is not None:
        return __CheckUsernameAvailability(
            message="username tidak tersedia",
            code=2,
            is_available=False,
        )

    return __CheckUsernameAvailability(
        message="username tersedia",
        code=0,
        is_available=True,
    )
