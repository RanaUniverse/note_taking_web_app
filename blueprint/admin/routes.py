"""
blueprint/admin/routes.py
I make this for now where i want to see some admin related informations
Which are accessable by the admins here in my app.
"""

from flask import (
    Blueprint,
    render_template,
    flash
)

from db_codes.database_make import engine
from db_codes.db_functions import (
    get_all_user_list,
    get_user_obj_from_username,
    get_all_note_list,
    get_all_notes_from_user_id,
    
)

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
        "/admin/all_users_info.html",
        all_users=all_users,
    )


@admin_bp.route("/all_notes")
def all_notes_info():
    all_notes = get_all_note_list(engine=engine)
    return render_template(
        "/admin/all_notes_info.html",
        all_notes=all_notes,
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
        if not user_row:
            flash(f"User Has Not Found with, <u>{given_username}</u>", "error")
            return render_template(
                "/admin/user_info.html",
                user=user_row,
                form=form,
            )

        user_id = user_row.user_id
        his_notes = get_all_notes_from_user_id(
            engine=engine,
            user_id=user_id,
        )
        flash(f"User Details For {given_username}", "success")
        return render_template(
            "/admin/user_info.html",
            user=user_row,
            notes=his_notes,
            form=form,
        )

    return render_template(
        "/admin/user_from_username.html",
        form=form,
    )
