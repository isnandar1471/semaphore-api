import uuid
import time
import typing

import sqlalchemy
import sqlalchemy.orm


from ..config import constant
from ..model import article_model


engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
session = sqlalchemy.orm.Session(engine)


def select_all():
    # engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    # session = sqlalchemy.orm.Session(engine)
    result = []
    try:
        result = session.query(article_model.ArticleModel).all()
    except Exception as e:
        print(e)
    finally:
        session.close()

    return result


def select_one_by_id(id: uuid.UUID):
    # engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    # session = sqlalchemy.orm.Session(engine)

    result = None
    try:
        result = session.query(article_model.ArticleModel).get(id)
    except Exception as e:
        print(e)
    finally:
        session.close()

    return result


def select_latest_article(total: int):
    # engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    # session = sqlalchemy.orm.Session(engine)

    latest_article = []
    try:
        latest_article = session.query(article_model.ArticleModel).order_by(article_model.ArticleModel.created_at.desc()).limit(total).all()
    except Exception as e:
        print(e)
    finally:
        session.close()

    return latest_article


def update_one_by_id(
    id: uuid.UUID,
    title: article_model.ArticleModel.title | None,
    cover_url: article_model.ArticleModel.cover_url | None,
    description: article_model.ArticleModel.description | None,
    article_url: article_model.ArticleModel.article_url | None,
):
    #     engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    #     session = sqlalchemy.orm.Session(engine)

    current_article: article_model.ArticleModel | None = session.query(article_model.ArticleModel).get(id)

    if not current_article:
        return False

    if title:
        current_article.title = title

    if cover_url:
        current_article.cover_url = cover_url

    if description:
        current_article.description = description

    if article_url:
        current_article.article_url = article_url

    current_article.updated_at = int(time.time())

    session.commit()

    return True


def insert(
    title,
    cover_url,
    description,
    article_url,
):
    id = uuid.uuid4()
    current_article = article_model.ArticleModel(
        id=id,
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
        created_at=int(time.time()),
        updated_at=None,
    )

    # engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    # session = sqlalchemy.orm.Session(engine)

    is_success = False
    try:
        session.add(current_article)
        session.commit()
        is_success = True
    except Exception as e:
        print(e)
    finally:
        session.close()

    if is_success:
        return id
    return None


def delete_by_id(id: uuid.UUID):
    # engine = sqlalchemy.create_engine(constant.DATABASE_URL_ENGINE)
    # session = sqlalchemy.orm.Session(engine)

    is_success = False
    try:
        article_to_delete: article_model.ArticleModel | None = session.query(article_model.ArticleModel).get(id)
        if article_to_delete:
            session.delete(article_to_delete)
            session.commit()

            is_success = True
    except Exception as e:
        print(e)
    finally:
        session.close()

    return is_success
