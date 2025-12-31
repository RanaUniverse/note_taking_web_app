"""
Here i will write code which will do the work
Of Some Database Functions to interect with DB.

And the main logic is i will call this function
and it will work in my main places.

"""

from sqlalchemy import Engine
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from db_codes.models_table import UserData, NoteData

from utils.custom_logger import logger


def add_new_user(
    engine: Engine,
    user_row: UserData,
) -> UserData | None:
    """
    I will call this function and pass the user_obj
    and it will try to insert the data in the table and
    return the new user_obj which i can use.
    """
    with Session(engine) as session:
        try:
            session.add(user_row)
            session.commit()
            session.refresh(user_row)
            return user_row

        except IntegrityError as e:
            logger.warning(e)
            return None

        except Exception as e:
            logger.error(e)
            return None


def add_new_note(
    engine: Engine,
    user_row: UserData,
    note_title: str,
    note_content: str,
) -> NoteData | None:
    """
    Here i assume that the user is already present in the table
    i need to pass the user_obj and the note details to insert in the db
    """

    note_obj = NoteData(
        note_title=note_title,
        note_content=note_content,
    )
    with Session(engine) as session:
        try:
            note_obj.user = user_row

            session.add(note_obj)
            session.commit()
            session.refresh(note_obj)
            return note_obj

        except IntegrityError as e:
            logger.warning(e)
            return None

        except Exception as e:
            logger.error(e)
            return None


def get_all_user_list(engine: Engine):
    with Session(engine) as session:
        statement = select(UserData)
        results = session.exec(statement)
        all_user = results.all()
        return all_user


def get_user_obj_from_user_id(
    engine: Engine,
    user_id: str,
) -> UserData | None:
    """
    If the user id is wrong or the user row not found
    against this user_id it will return none
    """
    with Session(engine) as session:
        sta = select(UserData).where(UserData.user_id == user_id)
        results = session.exec(sta)
        one_user = results.first()
        return one_user


def get_user_obj_from_username(
    engine: Engine,
    username: str,
) -> UserData | None:
    """
    Here i will pass the username and it should take out
    the user obj and show me this
    """
    with Session(engine) as session:
        sta = select(UserData).where(UserData.username == username)
        results = session.exec(sta)
        one_user = results.first()
        return one_user


def get_all_notes_from_user_id(
    engine: Engine,
    user_id: str,
):
    with Session(engine) as session:
        sta = select(UserData).where(UserData.user_id == user_id)
        results = session.exec(sta)
        one_user = results.first()
        if not one_user:
            return
        return one_user.notes


def get_all_notes_from_user_obj(
    engine: Engine,
    user_obj: UserData,
):
    """
    Maybe i will not use this in warning?

    When there is a valid correct user_obj i will pass the obj
    and it will give me the list of all his notes
    """
    with Session(engine) as session:
        statement = select(NoteData).where(NoteData.user_id == user_obj.user_id)
        results = session.exec(statement)
        return results.all()
