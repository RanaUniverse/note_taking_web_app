"""
blueprint/admin/routes.py
I make this for now where i want to see some admin related informations
Which are accessable by the admins here in my app.
"""

from flask import (
    Blueprint,
    render_template,
)

from db_codes.database_make import engine
from db_codes.db_functions import get_all_user_list, get_user_obj_from_username

from wft_forms_fillup import UserFromUsernameForm

admin_bp = Blueprint(
    name="admin_bp",
    import_name=__name__,
    template_folder="templates",
)


@admin_bp.route("/")
def index_page():
    return render_template("/admin/index.html")


@admin_bp.route("/all_users")
def all_users_info():
    all_users = get_all_user_list(engine=engine)
    return render_template(
        "/admin/users_info.html",
        all_users=all_users,
    )


@admin_bp.route("/note_count")
def note_count():

    return render_template(
        "/admin/notes_count.html",
    )


@admin_bp.route("/user_from_username", methods=["GET", "POST"])
def username():
    # first here i will check if this req came from the admin
    # for now i am keep this simepl nothings checking yet

    form = UserFromUsernameForm()
    if form.validate_on_submit():  # type: ignore
        given_username: str = form.username.data or ""
        if not given_username:
            return "You havenot passed any username yet."
        user_row = get_user_obj_from_username(
            engine=engine,
            username=given_username,
        )
        return render_template(
            "/admin/user_info.html",
            user_row=user_row,
        )

    return render_template(
        "/admin/user_from_username.html",
        form=form,
    )
