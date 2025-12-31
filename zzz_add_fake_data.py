"""
This file i will run it will cause the fake data will insert in my db
zzz_add_fake_data.py
"""

from faker import Faker


from db_codes.database_make import engine
from db_codes.db_functions import add_new_user, add_new_note
from db_codes.models_table import UserData

fake = Faker()


print(
    "This code is inserting some demo data in the database "
    "on each run it will insert new user and new note"
)


def insert_one_demo_user():
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


def inser_one_demo_note(user_obj: UserData):
    note_title = fake.sentence(3)
    note_content = fake.paragraph(10)
    note_row = add_new_note(
        engine=engine,
        user_row=user_obj,
        note_title=note_title,
        note_content=note_content,
    )
    return note_row


if __name__ == "__main__":
    user = insert_one_demo_user()
    if not user:
        print("user insert has not successful")
        exit()

    inser_one_demo_note(user)
