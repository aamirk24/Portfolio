from flask import Blueprint, Response, abort, render_template, url_for

from app.data.projects import (
    CAPABILITIES,
    EDUCATION,
    EXPERIENCE,
    FEATURED_PROJECTS,
    get_adjacent_projects,
    get_project,
)


main = Blueprint("main", __name__)


@main.get("/")
def index():
    """Render the portfolio landing page."""
    return render_template(
        "index.html",
        capabilities=CAPABILITIES,
        education=EDUCATION,
        experience=EXPERIENCE,
        featured_projects=FEATURED_PROJECTS,
    )


@main.get("/projects/<slug>", strict_slashes=False)
def project_detail(slug):
    """Render a project case study from its structured content."""
    project = get_project(slug)

    if project is None:
        abort(404)

    previous_project, next_project = get_adjacent_projects(slug)
    project_number = next(
        index
        for index, featured_project in enumerate(FEATURED_PROJECTS, start=1)
        if featured_project["slug"] == slug
    )

    return render_template(
        "project_detail.html",
        project=project,
        project_number=project_number,
        project_total=len(FEATURED_PROJECTS),
        previous_project=previous_project,
        next_project=next_project,
    )


@main.get("/robots.txt")
def robots():
    """Expose crawler guidance with the environment's canonical sitemap URL."""
    sitemap_url = url_for("main.sitemap", _external=True)
    return Response(
        f"User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n",
        mimetype="text/plain",
    )


@main.get("/sitemap.xml")
def sitemap():
    """List the public portfolio routes for search engines."""
    return Response(
        render_template("sitemap.xml", featured_projects=FEATURED_PROJECTS),
        mimetype="application/xml",
    )
