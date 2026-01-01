"""
This file i will run it will cause the fake data will insert in my db
This file will need to run after run the main.py
zzz_insert_demo_data.py
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
    USER_COUNT = 3
    NOTE_COUNT = 5

    for _ in range(USER_COUNT):
        user = insert_one_demo_user()

        if not user:
            print("user insert has Declined ❌")
            continue

        for _ in range(NOTE_COUNT):
            insert_one_demo_note(user)

    print(f"{USER_COUNT} users and {USER_COUNT * NOTE_COUNT} notes inserted.")
