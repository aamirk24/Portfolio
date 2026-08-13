"""Render the Flask portfolio into a static Cloudflare Pages build."""

import os
import shutil
from pathlib import Path

from app import create_app
from app.data.projects import FEATURED_PROJECTS


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIRECTORY = PROJECT_ROOT / "dist"


def build_site(output_directory=DEFAULT_OUTPUT_DIRECTORY, site_url=None):
    """Build every public route and copy assets into the output directory."""
    output_directory = Path(output_directory)
    site_url = (
        site_url
        or os.getenv("SITE_URL")
        or os.getenv("CF_PAGES_URL")
        or "http://localhost"
    ).rstrip("/")

    if output_directory.exists():
        shutil.rmtree(output_directory)

    output_directory.mkdir(parents=True)

    app = create_app({"TESTING": True})
    routes = [
        ("/", "index.html", 200),
        *(
            (f"/projects/{project['slug']}", f"projects/{project['slug']}/index.html", 200)
            for project in FEATURED_PROJECTS
        ),
        ("/robots.txt", "robots.txt", 200),
        ("/sitemap.xml", "sitemap.xml", 200),
        ("/not-found", "404.html", 404),
    ]

    with app.test_client() as client:
        for route, destination, expected_status in routes:
            response = client.get(route, base_url=site_url)
            if response.status_code != expected_status:
                raise RuntimeError(
                    f"Static build failed for {route}: expected {expected_status}, "
                    f"received {response.status_code}."
                )

            destination_path = output_directory / destination
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            destination_path.write_bytes(response.data)

    shutil.copytree(PROJECT_ROOT / "app" / "static", output_directory / "static")
    shutil.copy2(PROJECT_ROOT / "cloudflare" / "_headers", output_directory / "_headers")

    return output_directory


if __name__ == "__main__":
    built_directory = build_site()
    print(f"Static portfolio built in {built_directory}")
