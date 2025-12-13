from flask import Flask, render_template, request
from flask_login import UserMixin, LoginManager  # type: ignore
from login_form_making import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"


# Below the first one str is the user id, this is different than
# username, as username mabye change for this user by his own wish which is str
DEMO_USERS: dict[str, dict[str, str | int]] = {
    "a": {
        "id": "a",
        "username": "a",
        "email": "a@a.a",
        "password": "a",
        "phone_no": 9876543210,
    },
    "b": {
        "id": "b",
        "username": "b",
        "email": "b@b.b",
        "password": "b",
        "phone_no": 9876543210,
    },
    "rana": {
        "id": "rana",
        "username": "rana",
        "email": "rana@example.com",
        "password": "1234",
        "phone_no": 9876543210,
    },
    "admin": {
        "id": "admin",
        "username": "admin",
        "email": "admin@example.com",
        "password": "admin",
        "phone_no": 9876543210,
    },
    "user1": {
        "id": "user1",
        "username": "user1",
        "email": "user1@example.com",
        "password": "pass1",
        "phone_no": 9876543210,
    },
    "user2": {
        "id": "user2",
        "username": "user2",
        "email": "user2@example.com",
        "password": "pass2",
        "phone_no": 9876543210,
    },
}


login_manager = LoginManager()
login_manager.login_view = "login"  # type: ignore
login_manager.init_app(app)  # type: ignore


class DemoUser(UserMixin):
    def __init__(self, id: str, username: str):
        self.id = id
        self.username = username


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
    )


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about_page.html")


@app.route("/help")
def help_page():
    return render_template("help_page.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":

        return "You have submitted your information. <br> we will contact you back"
        ...

    return render_template(
        "login.html",
        form=form,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
