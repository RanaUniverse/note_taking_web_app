"""
Here i will write code which will do the work
Of Some Database Functions to interect with DB.

And the main logic is i will call this function
and it will work in my main places.

"""

from sqlalchemy import Engine
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from db_codes.models_table import UserData, NoteData
from utils.demo_data import print_red


def add_new_user(engine: Engine, user_row: UserData) -> UserData | None:
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
            print_red(str(e))
            return None


def add_new_note(
    engine: Engine,
    user_row: UserData,
    note_title: str,
    note_content: str,
) -> NoteData | None:
    """
    Here i assume that the user is already present in the table
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
            print_red(str(e))
            return None
