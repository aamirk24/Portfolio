import pytest

from app.data.projects import FEATURED_PROJECTS


def test_homepage_contains_primary_recruiter_content(client):
    response = client.get("/")
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "I’m Aamir Khan." in page
    assert "aamirk2405@gmail.com" in page
    assert "https://github.com/aamirk24" in page
    assert "https://www.linkedin.com/in/aamirkhan05/" in page
    assert "Aamir_Khan_Software_Engineering_CV.pdf" in page
    assert 'data-project-universe' in page

    for project in FEATURED_PROJECTS:
        assert project["title"] in page
        assert f'/projects/{project["slug"]}' in page


@pytest.mark.parametrize(
    "project",
    FEATURED_PROJECTS,
    ids=[project["slug"] for project in FEATURED_PROJECTS],
)
def test_each_case_study_is_available(client, project):
    response = client.get(f'/projects/{project["slug"]}')
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert f'{project["title"]} | Aamir Khan' in page
    assert project["summary"] in page
    assert project["overview"] in page

    if project.get("hero_image"):
        assert project["hero_image"] in page
        assert project["hero_image_alt"] in page
    if project.get("secondary_image"):
        assert project["secondary_image"] in page
        assert project["secondary_image_alt"] in page


def test_unknown_project_returns_not_found(client):
    response = client.get("/projects/unknown-project")

    assert response.status_code == 404
    assert b"Page not found." in response.data
    assert b"Return home" in response.data


def test_pages_include_contextual_metadata(client):
    homepage = client.get("/")
    project = client.get("/projects/scholargraph")

    assert b'<link rel="canonical" href="http://localhost/">' in homepage.data
    assert b'<meta property="og:type" content="website">' in homepage.data
    assert b'<meta property="og:type" content="article">' in project.data
    assert b"A research platform that connects academic metadata" in project.data


def test_security_and_cache_headers(client):
    page = client.get("/")
    asset = client.get("/static/css/main.css")

    assert "default-src 'self'" in page.headers["Content-Security-Policy"]
    assert page.headers["X-Content-Type-Options"] == "nosniff"
    assert page.headers["X-Frame-Options"] == "DENY"
    assert page.headers["Cache-Control"] == "no-cache"
    assert asset.headers["Cache-Control"] == "public, max-age=3600, must-revalidate"


def test_discovery_files_list_every_project(client):
    robots = client.get("/robots.txt")
    sitemap = client.get("/sitemap.xml").get_data(as_text=True)

    assert robots.status_code == 200
    assert b"Sitemap: http://localhost/sitemap.xml" in robots.data
    for project in FEATURED_PROJECTS:
        assert f'http://localhost/projects/{project["slug"]}' in sitemap


def test_cv_download_is_available(client):
    response = client.get(
        "/static/documents/Aamir_Khan_Software_Engineering_CV.pdf"
    )

    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert response.data.startswith(b"%PDF")
