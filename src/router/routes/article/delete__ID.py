from uuid import UUID

import fastapi
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_200_OK,
)

from src.schema.base_schema import Response
from src.service.article_service import delete_by_id

router = fastapi.APIRouter()


@router.delete("/{id}")
def delete_article_by_id(id: str):
    is_success, error = delete_by_id(UUID(hex=id))

    if error is not None:
        return JSONResponse(
            content=Response(
                code=1,
                message="Gagal menghapus artikel",
            ).model_dump(),
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return JSONResponse(
        content=Response(
            code=0,
            message="Berhasil menghapus artikel",
        ).model_dump(),
        status_code=HTTP_200_OK,
    )
