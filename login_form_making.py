"""
This is Login form fillup
"""

from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    This will be the my custom login form which i will use
    """

    username = StringField(label="Username or Email ID", validators=[DataRequired()])
    password = PasswordField(label="Your Password", validators=[DataRequired()])
    submit = SubmitField(label="Login Here")
