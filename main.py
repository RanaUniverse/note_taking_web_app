"""
This is my main.py code which i will run
"""

import sys

sys.dont_write_bytecode = True
# This upper 2 line not make the __pycache__ folder


from flask import (
    Flask,
)
from flask_login import (  # type: ignore
    LoginManager,
)


from blueprint.auth.routes import auth_bp
from blueprint.note.routes import note_bp
from blueprint.general.routes import general_bp
from blueprint.profile.routes import profile_bp
from blueprint.admin.routes import admin_bp

from utils.demo_data import DEMO_USERS, DemoUser


from db_codes.database_make import create_db_and_engine

app = Flask(__name__)

app.config["SECRET_KEY"] = "super-secret-key"

app.register_blueprint(blueprint=auth_bp)
app.register_blueprint(blueprint=general_bp)
app.register_blueprint(blueprint=note_bp)
app.register_blueprint(blueprint=profile_bp)
app.register_blueprint(blueprint=admin_bp, url_prefix="/admin")

login_manager = LoginManager()
login_manager.login_view = "auth_bp.login"  # type: ignore
login_manager.init_app(app)  # type: ignore


@login_manager.user_loader  # type: ignore
def load_demo_users(user_id: str):
    """
    This Function is said to make in such a way it must return none
    when user not active not want to login for htis user
    """
    user_data = DEMO_USERS.get(user_id, None)
    if not user_data:
        return None

    return DemoUser(
        id=str(user_data["id"]),
        username=str(user_data["username"]),
        email=str(user_data["email"]),
    )


if __name__ == "__main__":
    create_db_and_engine()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
