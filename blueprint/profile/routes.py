"""
Here i will keep the dashboard & profile
related code so that it will help me to separate the
profile related informations in this file
blueprint/profile/routes.py
"""

from flask import Blueprint, render_template

from flask_login import (  # type:ignore
    login_required,  # type: ignore
    current_user,
)

from utils.demo_data import DEMO_NOTES

profile_bp = Blueprint(
    name="profile_bp",
    import_name=__name__,
    template_folder="templates",
)


@profile_bp.route("/dashboard")
@login_required
def dashboard():
    user_id = current_user.id
    user_notes = DEMO_NOTES.get(user_id, [])
    return render_template(
        "dashboard.html",
        notes=user_notes,
    )


@profile_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html")
