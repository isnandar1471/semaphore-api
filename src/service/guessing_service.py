import typing
import time
import os
import random


import uuid
import sqlalchemy


import src.orm.guessing
import src.config.database
import src.config.constant


def get_guessing_by_id(guessing_id: str) -> typing.Tuple[bool, typing.Union[src.orm.guessing.GuessingOrm, None], typing.Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    result: typing.Union[src.orm.guessing.GuessingOrm, None] = None
    error: typing.Union[Exception, None] = None
    try:
        result = session.query(src.orm.guessing.GuessingOrm).get(guessing_id)
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, result, error


def predict_guessing_by_id(guessing_id: str, predicted_value: str) -> typing.Tuple[bool, typing.Union[Exception, None]]:
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
            sqlalchemy.update(src.orm.guessing.GuessingOrm)
            .where(src.orm.guessing.GuessingOrm.id == guessing_id)
            .values(
                predicted_at=time.time(),
                updated_at=time.time(),
                predicted_value=predicted_value,
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


def new_guessing_from_param(
    filepath: str,
    actual_value: str,
    id: typing.Optional[typing.Union[str, uuid.UUID]] = None,
    user_id: typing.Optional[typing.Union[str, uuid.UUID]] = None,
    created_at: typing.Optional[float] = None,
    predicted_value: typing.Optional[str] = None,
    predicted_at: typing.Optional[float] = None,
    updated_at: typing.Optional[float] = None,
):
    guessing_inst = src.orm.guessing.GuessingOrm(
        id=str(id if id != None else uuid.uuid4()),
        user_id=str(user_id) if user_id != None else None,
        filepath=filepath,
        actual_value=actual_value,
        created_at=created_at if created_at != None else time.time(),
        predicted_value=predicted_value,
        predicted_at=predicted_at,
        updated_at=updated_at,
    )
    return new_guessing_from_instance(guessing_inst=guessing_inst)


def new_guessing_from_instance(guessing_inst: src.orm.guessing.GuessingOrm) -> typing.Tuple[bool, src.orm.guessing.GuessingOrm, typing.Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success: bool = False
    error: typing.Union[Exception, None] = None
    try:
        session.add(guessing_inst)
        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, guessing_inst, error


def random_file() -> typing.Tuple[typing.Union[Exception, None], typing.Union[str, None], typing.Union[typing.List[str], None]]:
    """
    return (
        str: choosed_char,
        str: choosed_filepath
        )
    """

    choosed_char: str
    try:
        choosed_char = random.choice(src.config.constant.CLASSES).lower()
    except Exception as e:
        return e, None, None

    choosed_dirpath = os.path.join(src.config.constant.GUESSING_DIRPATH, choosed_char)

    list_of_dirpath = get_file_paths(directory=choosed_dirpath)

    choosed_filepath: str
    try:
        choosed_filepath = random.choice(list_of_dirpath)
    except Exception as e:
        return e, None, None

    arr_of_path = choosed_filepath.replace(src.config.constant.GUESSING_DIRPATH, "").replace("\\", "/").split("/")
    if arr_of_path[0] == "":
        del arr_of_path[0]

    return None, choosed_char, arr_of_path


def get_file_paths(directory: str) -> typing.List[str]:
    file_paths: typing.List[str] = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path: str = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths
