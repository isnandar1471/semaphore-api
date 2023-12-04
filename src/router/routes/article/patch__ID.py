import typing
import uuid
import http


import fastapi


import src.service.article_service
import src.schema.base_schema
import src.orm.article


class OutPatchId(src.schema.base_schema.Response):
    data: typing.Union[src.orm.article.ArticleSchema, None]


router = fastapi.APIRouter()


@router.patch("/{id}")
def update_article_by_id(
    id: str,
    title: typing.Annotated[typing.Union[str, None], fastapi.Form()] = None,
    cover_url: typing.Annotated[typing.Union[str, None], fastapi.Form()] = None,
    description: typing.Annotated[typing.Union[str, None], fastapi.Form()] = None,
    article_url: typing.Annotated[typing.Union[str, None], fastapi.Form()] = None,
):
    is_success, current_article, error = src.service.article_service.update_one_by_id(
        uuid.UUID(hex=id),
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
    )

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutPatchId(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if current_article == None:
        return fastapi.responses.JSONResponse(
            content=OutPatchId(
                message=f"article tidak ditemukan",
                code=2,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.BAD_REQUEST,
        )

    return fastapi.responses.JSONResponse(
        content=OutPatchId(
            message=f"berhasil mengubah artikel",
            code=3,
            data=current_article,
        ).model_dump(),
        status_code=http.HTTPStatus.OK,
    )
