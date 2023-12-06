import typing
import http


import fastapi


import src.service.article_service
import src.orm.article
import src.service.mapping
import src.schema.base_schema


class OutGetAllArticle(src.schema.base_schema.Response):
    data: typing.Union[typing.List[src.orm.article.ArticleSchema], None]


router = fastapi.APIRouter()


@router.get("/")
def get_all_article():
    is_success, all_articles, error = src.service.article_service.select_all(latest_first=True)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutGetAllArticle(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if is_success == False:
        return fastapi.responses.JSONResponse(
            content=OutGetAllArticle(
                message="gagal mendapatkan article",
                code=2,
                data=None,
            ).model_dump(),
            status_code=400,
        )

    returned_article = []

    for article_orm in all_articles:
        article_schema: typing.Union[src.orm.article.ArticleSchema, None] = None
        try:
            article_schema = src.orm.article.ArticleSchema.model_validate(article_orm)
        except Exception as e:
            print("🚀 ~ file: get__.py:55 ~ e.args:", e)

        returned_article.append(article_schema)

    return fastapi.responses.JSONResponse(
        content=OutGetAllArticle(
            message="berhasil mendapatkan artikel",
            code=0,
            data=returned_article,
        ).model_dump(),
        status_code=http.HTTPStatus.OK,
    )
