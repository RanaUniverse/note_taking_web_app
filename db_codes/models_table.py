"""
This is models_table.py
Here i will keep the logic of making the user and note class
and then i will use those class for making functions.
"""

import datetime

from sqlmodel import (
    Field,  # type: ignore
    SQLModel,
    Relationship,
)


from utils.needy_things import GMT_TIMEZONE
from utils.needy_things import generate_uuid


class UserData(SQLModel, table=True):
    __tablename__: str = "user_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(default_factory=generate_uuid, index=True)
    username: str | None = Field(default=None, index=True, unique=True)
    first_name: str | None = Field(default=None)
    last_name: str | None = Field(default=None)
    email_id: str | None = Field(default=None)
    phone_no: str | None = Field(default=None)

    account_creation_time: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(GMT_TIMEZONE),
    )

    notes: list["NoteData"] = Relationship(back_populates="user")


class NoteData(SQLModel, table=True):
    __tablename__: str = "note_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    note_id: str = Field(default_factory=generate_uuid, unique=True, index=True)
    # Use a lambda function for unique id i will for each note.
    note_title: str | None = Field(default=None)
    note_content: str | None = Field(default=None)

    user_id: str = Field(default=None, foreign_key="user_data.user_id")

    created_time: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(GMT_TIMEZONE),
    )
    edited_time: datetime.datetime | None = Field(default=None)
    is_available: bool = Field(default=True)

    user: UserData = Relationship(back_populates="notes")
