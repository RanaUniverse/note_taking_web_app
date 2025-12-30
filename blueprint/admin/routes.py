"""
blueprint/admin/routes.py
I make this for now where i want to see some admin related informations
Which are accessable by the admins here in my app.
"""

from flask import (
    Blueprint,
    render_template,
)

admin_bp = Blueprint(
    name="admin_bp",
    import_name=__name__,
    template_folder="templates",
)


@admin_bp.route("/")
def index_page():
    return render_template("/admin/index.html")


@admin_bp.route("/note_count")
def note_count():
    return render_template("/admin/notes_count.html")
