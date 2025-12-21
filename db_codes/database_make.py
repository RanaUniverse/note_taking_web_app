"""
This is the engine part having the engine to use
and it will have a table making fun
this will just a helper module which will be used to create the db file
'engine' this need to import from this file
i need to import `create_db_and_engine()`
"""

from pathlib import Path


from sqlmodel import (
    create_engine,
    SQLModel,
)


# just this 2 import is necessary to make the table in the .db file
from db_codes.models_table import (
    UserData,  # type: ignore
    NoteData,  # type: ignore
)


from utils.needy_things import DATABASE_FILE_NAME


sqlite_file_name = Path.cwd() / DATABASE_FILE_NAME

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(url=sqlite_url)


def create_db_and_engine():
    """
    When i will call this function it will make the database file,
    i need to call this in the main.py beginning
    """
    sqlite_file_name.parent.mkdir(exist_ok=True)
    SQLModel.metadata.create_all(engine)
