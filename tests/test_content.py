import hashlib
from pathlib import Path

import pytest

from app.data.projects import (
    FEATURED_PROJECTS,
    get_adjacent_projects,
    get_project,
)


@pytest.mark.parametrize(
    "project",
    FEATURED_PROJECTS,
    ids=[project["slug"] for project in FEATURED_PROJECTS],
)
def test_each_published_case_study_is_available(client, project):
    response = client.get(f"/projects/{project['slug']}")
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert f"{project['title']} | Aamir Khan" in page

    if project["repository_url"]:
        assert project["repository_url"] in page
        assert "View repository" in page
    else:
        assert "View repository" not in page


def test_project_content_contract_is_complete_and_unique():
    required_fields = {
        "slug",
        "title",
        "category",
        "year",
        "summary",
        "highlight",
        "technologies",
        "visual",
        "role",
        "repository_url",
        "overview",
        "contribution",
        "decisions",
        "outcomes",
    }
    slugs = [project["slug"] for project in FEATURED_PROJECTS]

    assert slugs
    assert len(slugs) == len(set(slugs))

    for project in FEATURED_PROJECTS:
        assert required_fields == project.keys()
        assert project["technologies"]
        assert project["decisions"]
        assert project["outcomes"]
        if project["repository_url"]:
            assert project["repository_url"].startswith("https://github.com/")


def test_project_lookup_and_navigation_cover_the_full_collection():
    for index, project in enumerate(FEATURED_PROJECTS):
        assert get_project(project["slug"]) is project

        previous_project, next_project = get_adjacent_projects(project["slug"])
        assert previous_project is FEATURED_PROJECTS[index - 1]
        assert next_project is FEATURED_PROJECTS[
            (index + 1) % len(FEATURED_PROJECTS)
        ]

    assert get_project("not-a-project") is None
    assert get_adjacent_projects("not-a-project") == (None, None)


def test_downloadable_cv_is_the_approved_file():
    cv_path = (
        Path(__file__).parents[1]
        / "app"
        / "static"
        / "documents"
        / "Aamir_Khan_Software_Engineering_CV.pdf"
    )

    assert cv_path.is_file()
    assert hashlib.sha256(cv_path.read_bytes()).hexdigest() == (
        "491b9edeaef348a7431682a5179ea202c9f36175b9936cbc5b13b890f1309939"
    )


def test_sitemap_lists_every_published_case_study(client):
    sitemap = client.get("/sitemap.xml").get_data(as_text=True)

    for project in FEATURED_PROJECTS:
        assert f"http://localhost/projects/{project['slug']}" in sitemap


def test_error_pages_are_excluded_from_search_results(client):
    response = client.get("/this-route-does-not-exist")
    page = response.get_data(as_text=True)

    assert response.status_code == 404
    assert '<meta name="robots" content="noindex, follow">' in page
