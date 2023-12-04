import uuid


import src.schema.response_schema
import src.orm.article


def article_out(article: src.orm.article.ArticleOrm):
    article_id: uuid.UUID = article.id

    return src.schema.response_schema.Article(
        id=article_id.hex,
        title=article.title,
        cover_url=article.cover_url,
        description=article.description,
        article_url=article.article_url,
        created_at=article.created_at,
        updated_at=article.updated_at,
    )
