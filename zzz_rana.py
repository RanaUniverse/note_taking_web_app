"""
This is for my learning checking codes...

Currently i can run this code and insert some fake data in the database
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from db_codes.database_make import engine
from db_codes.models_table import UserData
from db_codes.db_functions import add_new_user, add_new_note
from db_codes.models_table import NoteData


note_obj1 = NoteData(
    note_title="My Books",
    note_content="I have physics, math, english books",
)
note_obj2 = NoteData(
    note_title="My Phone",
    note_content="mi iphone vivo phones books",
)


def main():
    # a = get_user_obj_from_user_id(engine, user_id)
    # print(a)

    user_obj = UserData(
        username="sdfdsf",
        first_name="sdf",
        last_name="Univsdfdffiverse.com",
        phone_no="0453500",
    )

    # add_new_user(engine, user_obj)
    abc = add_new_user(engine=engine, user_row=user_obj)
    if not abc:
        return
    add_new_note(
        engine,
        abc,
        note_obj1.note_title,
        note_obj1.note_content,
    )
    add_new_note(
        engine,
        abc,
        note_obj2.note_title,
        note_obj2.note_content,
    )


if __name__ == "__main__":

    main()
