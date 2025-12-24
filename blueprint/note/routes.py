"""
Docstring for blueprint.note.routes
This i make to keep my notes related things here
blueprint/note/routes.py
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    url_for,
    render_template,
)
from flask_login import (  # type: ignore
    login_required,  # type: ignore
    current_user,
)

from wft_forms_fillup import NewNoteForm

from utils.demo_data import DEMO_NOTES

note_bp = Blueprint(
    name="note_bp",
    import_name=__name__,
    template_folder="templates",
)


@note_bp.route("/add-note", methods=["GET", "POST"])
@login_required
def add_note():
    form = NewNoteForm()

    if form.validate_on_submit():  # type: ignore
        user_id = current_user.id

        DEMO_NOTES.setdefault(user_id, []).append(
            {
                "title": form.title.data or "",
                "content": form.content.data or "",
            }
        )

        flash("Note added successfully ✅")
        return redirect(url_for("profile_bp.dashboard"))

    return render_template(
        "new_note_form.html",
        form=form,
    )
