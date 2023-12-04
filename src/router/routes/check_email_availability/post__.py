import typing


import fastapi


import src.service.user_service
import src.schema.base_schema


router = fastapi.APIRouter()


class __CheckEmailAvailability(src.schema.base_schema.Response):
    is_available: typing.Optional[bool]


@router.post("/")
def check_email_availability(
    email: typing.Annotated[str, fastapi.Form()],
):
    is_success, user_inst, error = src.service.user_service.find_user_by_email(email)
    if error != None:
        return __CheckEmailAvailability(
            message=f"server mengalami masalah: {error.args}",
            code=1,
            is_available=None,
        )

    if user_inst != None:
        return __CheckEmailAvailability(
            message="email tidak tersedia",
            code=2,
            is_available=False,
        )

    return __CheckEmailAvailability(
        message="email tersedia",
        code=0,
        is_available=True,
    )
