"""
This is for my learning checking codes...

Currently i can run this code and insert some fake data in the database
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from db_codes.models_table import UserData
from db_codes.db_functions import add_new_user, add_new_note
from db_codes.database_make import engine

user_obj = UserData(
    username="rana6",
    first_name="Rana",
    last_name="Universe",
    email_id="Rana@Universe.com",
    phone_no="000",
)

# add_new_user(engine, user_obj)
add_new_note(
    engine=engine,
    user_row=user_obj,
    note_title="Thansdfsdks",
    note_content="I am very glad to sesdfsde you",
)
