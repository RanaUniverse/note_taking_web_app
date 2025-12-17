"""
This is my main.py code which i will run
"""

from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from flask_login import (  # type: ignore
    UserMixin,
    LoginManager,
    login_user,  # type: ignore
    current_user,
    login_required,  # type: ignore
)

from wft_forms_fillup import LoginForm, NewNoteForm


def print_color(color_code: str | int, *msgs: str):
    print(f"\033[{color_code}m" + " ".join(map(str, msgs)) + "\033[0m")


def print_red(*msgs: str):
    print_color(31, *msgs)


def print_blue(*msgs: str):
    print_color(34, *msgs)


app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"


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


login_manager = LoginManager()
login_manager.login_view = "login"  # type: ignore
login_manager.init_app(app)  # type: ignore


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

    if form.validate_on_submit():  # type: ignore

        given_username: str = form.username.data or ""
        given_password = form.password.data or ""

        user_data = DEMO_USERS.get(given_username)
        print_red(
            given_username,
            given_password,
            user_data,  # type: ignore
        )

        if not user_data:
            print_blue("no usernme found")
            flash("The Username You Entered, is not exists in our database")
            flash("Please Check The Username Again")
            return redirect(url_for("login"))

        if user_data["password"] != given_password:
            print_blue("password not match")
            flash("The password you entered is not correct for this username")
            return redirect(url_for("login"))

        user_obj = DemoUser(
            id=str(user_data["id"]),
            username=str(user_data["username"]),
            email=str(user_data["email"]),
        )

        login_user(user_obj)

        next_page = request.args.get("next")
        return redirect(next_page or url_for("dashboard"))

    # below is when it will get request
    return render_template(
        "login_form.html",
        form=form,
    )


@app.route("/dashboard")
@login_required
def dashboard():
    user_id = current_user.id
    user_notes = DEMO_NOTES.get(user_id, [])
    return render_template(
        "dashboard.html",
        notes=user_notes,
    )


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@app.route("/add-note", methods=["GET", "POST"])
@login_required
def add_note():
    form = NewNoteForm()

    if form.validate_on_submit():  # type: ignore
        user_id = current_user.id
        print_blue("Old Note VAlues:", DEMO_NOTES)  # type: ignore

        DEMO_NOTES.setdefault(user_id, []).append(
            {
                "title": form.title.data or "",
                "content": form.content.data or "",
            }
        )

        print_red("New Note VAlues:", DEMO_NOTES)  # type: ignore

        flash("Note added successfully ✅")
        return redirect(url_for("dashboard"))

    return render_template(
        "new_note_form.html",
        form=form,
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
