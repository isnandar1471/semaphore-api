import http
import typing


import fastapi


import src.service.article_service
import src.service.mapping
import src.schema.base_schema
import src.orm.article


class OutGetCurrent(src.schema.base_schema.Response):
    data: typing.Union[typing.List[src.orm.article.ArticleSchema], None]


router = fastapi.APIRouter()


@router.get("/current")
def get_latest_article(total: int = 5):
    is_success, latest_article, error = src.service.article_service.select_latest_article(total)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutGetCurrent(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if is_success == False:
        return fastapi.responses.JSONResponse(
            content=OutGetCurrent(
                message="gagal mendapatkan article",
                code=2,
                data=None,
            ).model_dump(),
            status_code=400,
        )

    returned_article = []

    for article_orm in latest_article:
        article_schema: typing.Union[src.orm.article.ArticleSchema, None] = None
        try:
            article_schema = src.orm.article.ArticleSchema.model_validate(article_orm)
        except Exception as e:
            print("🚀 ~ file: get__.py:55 ~ e.args:", e)

        returned_article.append(article_schema)

    return fastapi.responses.JSONResponse(
        content=OutGetCurrent(
            message="berhasil mendapatkan artikel",
            code=0,
            data=returned_article,
        ).model_dump(),
        status_code=http.HTTPStatus.OK,
    )
