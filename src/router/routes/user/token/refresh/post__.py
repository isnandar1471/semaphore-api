import fastapi


# from ...... import config, schema, service
# import src.config
# import src.schema
# import


router = fastapi.APIRouter()


@router.post("/")
def refresh_token(
    refresh_token: str,
):
    pass
