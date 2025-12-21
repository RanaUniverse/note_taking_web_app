"""
Here i will keep the general pages
Ex. Index, About, Help page
blueprint/general/routes.py
"""

from flask import Blueprint, render_template


general_bp = Blueprint(
    name="general_bp",
    import_name=__name__,
    template_folder="templates",
)


@general_bp.route("/")
def index_page():
    return render_template("index.html")


@general_bp.route("/about")
def about_page():
    return render_template("about_page.html")


@general_bp.route("/help")
def help_page():
    return render_template("help_page.html")
