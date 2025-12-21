"""
This is my blueprint for the auth
blueprint/auth/routes.py is the file location for now
Here is: login, logout, register
"""

from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    request,
)

from flask_login import (  # type: ignore
    current_user,
    login_user,  # type: ignore
    login_required,  # type: ignore
    logout_user,
)


from utils.demo_data import print_blue, print_red, DemoUser, DEMO_USERS
from wft_forms_fillup import LoginForm

auth_bp = Blueprint(
    name="auth_bp",
    import_name=__name__,
    template_folder="templates",
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        print_blue("A Login user has open this /login")
        flash("You are already logged in.")
        flash("You don't need to login again")
        flash("You have been redirected to our /dashboard.")
        return redirect(url_for("profile_bp.dashboard"))

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
            return redirect(url_for("auth_bp.login"))

        if user_data["password"] != given_password:
            print_blue("password not match")
            flash("The password you entered is not correct for this username")
            return redirect(url_for("auth_bp.login"))

        user_obj = DemoUser(
            id=str(user_data["id"]),
            username=str(user_data["username"]),
            email=str(user_data["email"]),
        )
        print_blue("A user has just login here.")
        login_user(user_obj)

        next_page = request.args.get("next")
        return redirect(next_page or url_for("profile_bp.dashboard"))

    # below is when it will get request
    return render_template(
        "login_form.html",
        form=form,
    )


@auth_bp.route("/logout")
@auth_bp.route("/logout_me")
@login_required
def logout():
    username = current_user.username
    logout_user()
    flash(f"{username}, Recently You have been logout successfully...")
    return redirect(url_for("general_bp.index_page"))


@auth_bp.route("/register")
def register():
    flash("Coming Soon...")
    return render_template("register.html")
