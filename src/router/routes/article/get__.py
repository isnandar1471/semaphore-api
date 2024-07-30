from typing import Union, List

from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST

from src.orm.article import ArticleSchema
from src.schema.base_schema import Response as BaseResponse
from src.service.article_service import select_all


class OutGetAllArticle(BaseResponse):
    data: Union[List[ArticleSchema], None]


router = APIRouter()


@router.get("/", responses={
    HTTP_200_OK: {
        # "model": OutGetAllArticle,
        "content": {
            "application/json": {
                # "schema": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string"},
                        "code": {"type": "integer"},
                        "data": {"type": "array"},
                    }
                # }
            }
        }

    },
})
def get_all_article():
    is_success, all_articles, error = select_all(latest_first=True)

    if error:
        return JSONResponse(
            {
                "message": f"server error: {error.args}",
                "code": 1,
                "data": None,
            },
            HTTP_500_INTERNAL_SERVER_ERROR,
        )

    if not is_success:
        return JSONResponse(
            {
                "message": "gagal mendapatkan article",
                "code": 2,
                "data": None,
            },
            HTTP_400_BAD_REQUEST,
        )

    returned_article = []

    for article_orm in all_articles:
        article_schema: Union[ArticleSchema, None] = None
        try:
            article_schema = ArticleSchema.model_validate(article_orm)
        except Exception as e:
            print("🚀 ~ file: get__.py:55 ~ e.args:", e)

        returned_article.append(article_schema)

    return JSONResponse(
        {
            "message": "berhasil mendapatkan artikel",
            "code": 0,
            "data": returned_article,
        },
        HTTP_200_OK,
    )
