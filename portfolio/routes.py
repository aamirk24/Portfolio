from flask import Blueprint, render_template


main = Blueprint("main", __name__)


@main.get("/")
def index():
    """Render the portfolio landing page."""
    return render_template("index.html")
