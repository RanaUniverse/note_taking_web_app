"""
This is demo_data.py from here for now
i can import some checking data and variables
utils/demo_data.py
"""

from flask_login import UserMixin  # type: ignore


def print_color(color_code: str | int, *msgs: str):
    print(f"\033[{color_code}m" + " ".join(map(str, msgs)) + "\033[0m")


def print_red(*msgs: str):
    print_color(31, *msgs)


def print_blue(*msgs: str):
    print_color(34, *msgs)


# Below the first one str is the user id, this is different than
# username, as username mabye change for this user by his own wish which is str
DEMO_USERS: dict[str, dict[str, str | int]] = {
    "a": {
        "id": "a",
        "username": "a_extra",
        "full_name": "User A",
        "email": "a@a.a",
        "password": "a",
        "phone_no": 1111122222,
    },
    "b": {
        "id": "b",
        "username": "b_extra",
        "full_name": "User B",
        "email": "b@b.b",
        "password": "b",
        "phone_no": 1111133333,
    },
    "rana": {
        "id": "rana",
        "username": "rana",
        "full_name": "Rana",
        "email": "rana@example.com",
        "password": "1234",
        "phone_no": 999999999,
    },
    "admin": {
        "id": "admin",
        "username": "admin",
        "full_name": "Admin",
        "email": "admin@example.com",
        "password": "admin",
        "phone_no": 0,
    },
    "user1": {
        "id": "user1",
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "password": "pass1",
        "phone_no": 1212121212,
    },
    "user2": {
        "id": "user2",
        "username": "user2",
        "full_name": "User Two",
        "email": "user2@example.com",
        "password": "pass2",
        "phone_no": 1313131313,
    },
}


DEMO_NOTES: dict[str, list[dict[str, str]]] = {
    "rana": [
        {
            "title": "First Book",
            "content": "My First Book was Mathematics which i readed in childhood.",
        },
        {
            "title": "Second Book",
            "content": "My 2nd Experience was not memoriable",
        },
    ],
    "admin": [
        {
            "title": "Private Password",
            "content": "I am a admin so i will write some important information about my pass and so on here",
        },
        {
            "title": "Money Transfer",
            "content": "Here will be the informations of how much money i have spend where where",
        },
    ],
    "a": [
        {"title": "Learning NOte", "content": "This is the demo content i write here."}
    ],
    "b": [],
}


class DemoUser(UserMixin):
    def __init__(self, id: str, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

    @property
    def email_id(self):
        user_data = DEMO_USERS.get(self.id)
        return user_data.get("email_id") if user_data else None

    @property
    def full_name(self):
        user_data = DEMO_USERS.get(self.id)
        return user_data.get("full_name") if user_data else None

    @property
    def phone_no(self):
        user_data = DEMO_USERS.get(self.id)
        return user_data.get("phone_no") if user_data else None
