from flask import Blueprint, abort, render_template

from app.data.projects import FEATURED_PROJECTS, get_adjacent_projects, get_project


main = Blueprint("main", __name__)


@main.get("/")
def index():
    """Render the portfolio landing page."""
    return render_template("index.html", featured_projects=FEATURED_PROJECTS)


@main.get("/projects/<slug>")
def project_detail(slug):
    """Render a project case study from its structured content."""
    project = get_project(slug)

    if project is None:
        abort(404)

    previous_project, next_project = get_adjacent_projects(slug)

    return render_template(
        "project_detail.html",
        project=project,
        previous_project=previous_project,
        next_project=next_project,
    )
