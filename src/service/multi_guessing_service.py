import typing
import time
import os
import random


import uuid
import sqlalchemy


import src.config.environment
import src.orm.multi_guessing
import src.orm.guessing
import src.config.database
import src.config.constant


def get_multi_guessing_by_id(multi_guessing_id: str) -> typing.Tuple[bool, typing.Union[src.orm.multi_guessing.MultiGuessingOrm, None], typing.Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    result: typing.Union[src.orm.multi_guessing.MultiGuessingOrm, None] = None
    error: typing.Union[Exception, None] = None
    try:
        result = session.query(src.orm.multi_guessing.MultiGuessingOrm).get(multi_guessing_id)
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, result, error


def new_multi_guessing_from_instance(multi_guessing_inst: src.orm.multi_guessing.MultiGuessingOrm) -> typing.Tuple[bool, src.orm.multi_guessing.MultiGuessingOrm, typing.Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    error: typing.Union[Exception, None] = None
    try:
        session.add(multi_guessing_inst)
        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, multi_guessing_inst, error


# def get_random_word() -> typing.Tuple[typing.Union[Exception, None], str]:
#     """
#     return
#         Exception | None : error
#         str : word
#     """
#     error: typing.Union[Exception, None] = None
#     word = ""
#     try:
#         word = random.choice(src.config.constant.LIST_OF_WORDS)
#     except Exception as e:
#         error = e

#     return error, word


def predict_multi_guessing_by_id(multi_guessing_id: str, predicted_value: str) -> typing.Tuple[bool, typing.Union[Exception, None]]:
    """
    return
        bool: is_success
        Exception | None : error
    """
    session = src.config.database.SESSION_MAKER()

    is_success = False
    error: typing.Union[Exception, None] = None
    try:
        statement = (
            sqlalchemy.update(src.orm.multi_guessing.MultiGuessingOrm)
            .where(src.orm.multi_guessing.MultiGuessingOrm.id == multi_guessing_id)
            .values(
                predicted_at=time.time(),
                predicted_value=predicted_value,
                updated_at=time.time(),
            )
        )

        session.execute(statement)

        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, error
