"""
This file i will run it will cause the fake data will insert in my db
This file will need to run after run the main.py
zzz_insert_demo_data.py
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from faker import Faker


from db_codes.database_make import engine
from db_codes.db_functions import add_new_user, add_new_note
from db_codes.models_table import UserData

from utils.config_files import DEMO_NOTE_COUNT_INT, DEMO_USER_COUNT_INT

fake = Faker()


def insert_one_demo_user():
    try:
        user_obj = UserData(
            username=fake.user_name(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email_id=fake.email(),
            phone_no=fake.phone_number(),
        )
        user_row = add_new_user(
            engine=engine,
            user_row=user_obj,
        )
        return user_row

    except Exception as e:
        print(e)
        return None


def insert_one_demo_note(user_obj: UserData):
    try:
        note_title = fake.sentence(3)
        note_content = fake.paragraph(10)
        note_row = add_new_note(
            engine=engine,
            user_row=user_obj,
            note_title=note_title,
            note_content=note_content,
        )
        return note_row
    except Exception as e:
        print(e)
        return None


if __name__ == "__main__":
    USER_COUNT = DEMO_USER_COUNT_INT
    NOTE_COUNT = DEMO_NOTE_COUNT_INT

    print(
        "Inserting demo data into the database...\n"
        f"{USER_COUNT} users will be created, each with {NOTE_COUNT} notes."
    )

    for _ in range(USER_COUNT):
        user = insert_one_demo_user()

        if not user:
            print("user insert has Declined ❌")
            continue

        for _ in range(NOTE_COUNT):
            insert_one_demo_note(user)

    print(
        f"Successfully inserted {USER_COUNT} users and {USER_COUNT * NOTE_COUNT} notes into the database."
    )
