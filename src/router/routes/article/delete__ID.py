import uuid
import http


import fastapi


import src.service.article_service


router = fastapi.APIRouter()


@router.delete("/{id}")
def delete_article_by_id(id: str, response: fastapi.Response):
    is_success, error = src.service.article_service.delete_by_id(uuid.UUID(hex=id))

    if error is not None:
        response.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
        return is_success

    return is_success
