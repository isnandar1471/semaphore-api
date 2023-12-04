import typing


import fastapi
import pydantic


import src.config.environment
import src.router.index


class __OpenapiContact(pydantic.BaseModel):
    name: typing.Optional[str]
    url: typing.Optional[str]
    email: typing.Optional[str]


app = fastapi.FastAPI(
    title="-",
    description="-",
    redoc_url=None,
    docs_url="/docs" if src.config.environment.APP_ENABLE_APIDOC is True else None,
    contact=__OpenapiContact(
        name="Isnandar Fajar Pangestu",
        url="http://example.com/",
        email="isnandar.1471@gmail.com",
    ).model_dump(),
    debug=src.config.environment.APP_FASTAPI_DEBUG,
)


app.include_router(router=src.router.index.router)
