"""
This is Login form fillup
"""

from flask_wtf import FlaskForm  # type: ignore
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    This will be the my custom login form which i will use
    """

    username = StringField(
        label="Username or Email ID",
        validators=[DataRequired()],
    )
    password = PasswordField(
        label="Your Password",
        validators=[DataRequired()],
    )
    submit = SubmitField(label="Login Here")


class NewNoteForm(FlaskForm):
    """
    This will be when i wnat to take the data from user
    for making a new note and stores works mainly in the db
    """

    title = StringField(
        label="What is the subject of the note?",
        validators=[
            DataRequired(),
            Length(min=1, max=100),
        ],
    )
    content = TextAreaField(
        label="What is the content of your Note?",
        validators=[
            DataRequired(),
            Length(
                min=1,
                max=10000,
            ),
        ],
    )
    submit = SubmitField(label="Add This Note")
