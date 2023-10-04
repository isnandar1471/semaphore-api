import uuid


from ..model import article_model
from ..schema import response_schema


def article_out(article: article_model.ArticleModel):
    article_id: uuid.UUID = article.id

    return response_schema.ArticleOut(
        id=article_id.hex,
        title=article.title,
        cover_url=article.cover_url,
        description=article.description,
        article_url=article.article_url,
        created_at=article.created_at,
        updated_at=article.updated_at,
    )
