import typing
import http
import json

import fastapi


import src.service.article_service
import src.orm.article
import src.schema.base_schema


router = fastapi.APIRouter()


class __Out_Article(src.schema.base_schema.Response):
    data: typing.Optional[src.orm.article.ArticleSchema]


@router.post(
    "/",
    #  response_model=__Out_Article
)
def post_article(
    title: typing.Annotated[str, fastapi.Form()],
    cover_url: typing.Annotated[str, fastapi.Form()],
    description: typing.Annotated[str, fastapi.Form()],
    article_url: typing.Annotated[str, fastapi.Form()],
):
    is_success, article_inst, error = src.service.article_service.insert(
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
    )

    if error is not None:
        return fastapi.responses.JSONResponse(
            content=-__Out_Article(
                message=f"server mengalami error, {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if is_success is False:
        return fastapi.responses.JSONResponse(
            content=__Out_Article(
                message="gagal",
                code=2,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.BAD_REQUEST,
        )

    article_dto: typing.Optional[src.orm.article.ArticleSchema] = None

    try:
        article_dto = src.orm.article.ArticleSchema.model_validate(article_inst)
    except Exception as e:
        print(e)
        pass

    return fastapi.responses.JSONResponse(
        content=__Out_Article(
            message="sukses",
            code=0,
            data=article_dto,
        ).model_dump(),
        status_code=http.HTTPStatus.CREATED,
    )
