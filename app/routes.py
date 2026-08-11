from flask import Blueprint, render_template

from app.data.projects import FEATURED_PROJECTS


main = Blueprint("main", __name__)


@main.get("/")
def index():
    """Render the portfolio landing page."""
    return render_template("index.html", featured_projects=FEATURED_PROJECTS)
