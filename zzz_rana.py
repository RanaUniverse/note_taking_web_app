"""
This is for my learning checking codes...

Currently i can run this code and insert some fake data in the database
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from db_codes.database_make import engine
from db_codes.models_table import UserData
from db_codes.db_functions import (
    get_user_obj_from_user_id,
    add_new_user,
)
from db_codes.models_table import NoteData


note_obj = NoteData(
    note_title="My Books",
    note_content="I have physics, math, english books",
)

user_id = "2401ba966f844339a7a4b29442ab14cb"


def main():
    # a = get_user_obj_from_user_id(engine, user_id)
    # print(a)

    user_obj = UserData(
        username="rana6dsf",
        first_name="Rana",
        last_name="Universe",
        email_id="Rana@Universe.com",
        phone_no="000",
    )

    # add_new_user(engine, user_obj)
    add_new_user(engine=engine, user_row=user_obj)


if __name__ == "__main__":

    main()
