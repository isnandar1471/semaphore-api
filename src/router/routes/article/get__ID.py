import uuid
import typing
import http


import fastapi


import src.service.article_service
import src.service.mapping
import src.schema.base_schema
import src.orm.article


class OutGetId(src.schema.base_schema.Response):
    data: typing.Union[src.orm.article.ArticleSchema, None]


router = fastapi.APIRouter()


@router.get("/{id}")
def get_article_by_id(id: str):
    is_success, current_article, error = src.service.article_service.select_one_by_id(id)

    if error != None:
        return fastapi.responses.JSONResponse(
            content=OutGetId(
                message=f"server error: {error.args}",
                code=1,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )

    if is_success == False:
        return fastapi.responses.JSONResponse(
            content=OutGetId(
                message="gagal mendapatkan artikel",
                code=2,
                data=None,
            ).model_dump(),
            status_code=http.HTTPStatus.BAD_REQUEST,
        )

    if current_article == None:
        return fastapi.responses.JSONResponse(
            content=OutGetId(
                message="artikel tidak ditemukan",
                code=3,
                data=current_article,
            ).model_dump(),
            status_code=http.HTTPStatus.BAD_REQUEST,
        )

    article_schema: typing.Union[src.orm.article.ArticleSchema, None] = None

    try:
        article_schema = src.orm.article.ArticleSchema.model_validate(current_article)
    except Exception as e:
        print("🚀 ~ file: get__ID.py:54 ~ e.args:", e.args)

    return fastapi.responses.JSONResponse(
        content=OutGetId(
            message="berhasil mendapakan artikel",
            code=0,
            data=article_schema,
        ).model_dump(),
        status_code=http.HTTPStatus.OK,
    )
