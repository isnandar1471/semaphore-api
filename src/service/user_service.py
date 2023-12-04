import typing


import src.config.constant
import src.config.database
import src.orm.user


def create_new_user(user: src.orm.user.UserOrm) -> typing.Tuple[bool, typing.Union[Exception, None]]:
    """
    # Return

        first item is status. if operation success, will set to `True`. if operation failed, will set to 'False'

        second item is exception. if operation success, will set to `None`. if operation failed, will set to exception
    """

    session = src.config.database.SESSION_MAKER()
    is_success = False
    error: typing.Union[Exception, None] = None
    try:
        session.add(user)
        session.commit()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, error


def find_user_by_username(username: str) -> typing.Tuple[bool, typing.Union[src.orm.user.UserOrm, None], typing.Union[Exception, None]]:
    """
    # Return

        if operation success, will set to `UserModel`

        if operation failed, will set to `None`
    """

    session = src.config.database.SESSION_MAKER()

    is_success = False
    user_inst: typing.Union[src.orm.user.UserOrm, None] = None
    error: typing.Union[Exception, None] = None
    try:
        user_inst = session.query(src.orm.user.UserOrm).where(src.orm.user.UserOrm.username == username).first()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, user_inst, error


def find_user_by_email(email: str) -> typing.Tuple[bool, typing.Union[src.orm.user.UserOrm, None], typing.Union[Exception, None]]:
    session = src.config.database.SESSION_MAKER()

    is_success = False
    user_inst: typing.Union[src.orm.user.UserOrm, None] = None
    error: typing.Union[Exception, None] = None
    try:
        user_inst = session.query(src.orm.user.UserOrm).where(src.orm.user.UserOrm.email is email).first()
        is_success = True
    except Exception as e:
        error = e
    finally:
        session.close()

    return is_success, user_inst, error
