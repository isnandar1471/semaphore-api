import uuid
import time
import typing
from typing import (
    Tuple,
    Union,
    Optional
)

import src.config.constant
import src.orm.article
import src.config.database


def select_all(latest_first: bool = False) -> Tuple[bool, typing.List[src.orm.article.ArticleOrm], Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    result = []
    error = None
    try:
        query = session.query(src.orm.article.ArticleOrm)
        if latest_first:
            query = query.order_by(src.orm.article.ArticleOrm.created_at.desc())
        result = query.all()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, result, error


def select_one_by_id(article_id: str) -> Tuple[bool, Optional[src.orm.article.ArticleOrm], Optional[Exception]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    result: Optional[src.orm.article.ArticleOrm] = None
    error = None
    try:
        result = session.query(src.orm.article.ArticleOrm).get(article_id)
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, result, error


def select_latest_article(total: int) -> Tuple[bool, typing.List[src.orm.article.ArticleOrm], Optional[Exception]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    latest_article = []
    error = None
    try:
        latest_article = session.query(src.orm.article.ArticleOrm).order_by(src.orm.article.ArticleOrm.created_at.desc()).limit(total).all()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, latest_article, error


def update_one_by_id(
    article_id: uuid.UUID,
    title: Union[str, None],
    cover_url: Union[str, None],
    description: Union[str, None],
    article_url: Union[str, None],
) -> Tuple[bool, Union[src.orm.article.ArticleOrm, None], Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    current_article: Union[src.orm.article.ArticleOrm, None] = None
    error = None
    try:
        current_article = session.query(src.orm.article.ArticleOrm).get(article_id)
    except Exception as e:
        error = e

    if error is not None or current_article is None:
        return is_success, current_article, error

    if title is not None:
        current_article.title = title

    if cover_url is not None:
        current_article.cover_url = cover_url

    if description is not None:
        current_article.description = description

    if article_url is not None:
        current_article.article_url = article_url

    current_article.updated_at = time.time()

    try:
        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, current_article, error


def insert(
    title,
    cover_url,
    description,
    article_url,
) -> Tuple[bool, src.orm.article.ArticleOrm, Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    article_id = uuid.uuid4()
    current_article = src.orm.article.ArticleOrm(
        id=f"{article_id}",
        title=title,
        cover_url=cover_url,
        description=description,
        article_url=article_url,
        created_at=int(time.time()),
        updated_at=None,
    )
    error: Union[Exception, None] = None
    try:
        session.add(current_article)
        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.expunge(current_article)
        session.close()

    return is_success, current_article, error


def delete_by_id(article_id: uuid.UUID) -> Tuple[bool, Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    error: Optional[Exception] = None
    try:
        article_to_delete: Union[src.orm.article.ArticleOrm, None] = session.query(src.orm.article.ArticleOrm).get(article_id)
        if article_to_delete is not None:
            session.delete(article_to_delete)
            session.commit()

            is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, error
