from app import create_app


def test_create_app():
    app = create_app({"TESTING": True})

    assert app.config["TESTING"] is True


def test_homepage(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "I’m Aamir Khan.".encode() in response.data
    assert b"I build across" in response.data
    assert b"software engineering." in response.data
    assert b"data systems." in response.data
    assert b"applied AI." in response.data
    assert b"data-blueprint-field" in response.data
    assert b"data-headline-rotator" in response.data
    assert b"aamirk2405@gmail.com" in response.data
    assert b"https://github.com/aamirk24" in response.data
    assert b"https://www.linkedin.com/in/aamirkhan05/" in response.data
    assert response.data.count(b"Aamir_Khan_Software_Engineering_CV.pdf") == 4
    assert b'class="project-card"' not in response.data
    assert b"ScholarGraph" in response.data
    assert b"Nonaga" in response.data
    assert b"RepIT" in response.data
    assert b"Flip" in response.data
    assert b"Movie Genre Classification" in response.data
    assert b"VibeCheck" in response.data
    assert b"Curious across disciplines. Grounded in engineering." in response.data
    assert b"First-Class Computer Science graduate from the University of Leeds" in response.data
    assert response.data.count(b'class="capability-item"') == 3
    assert b"Software engineering" in response.data
    assert b"Data systems" in response.data
    assert b"Applied AI &amp; ML" in response.data
    assert response.data.count(b'class="technology-mark"') == 18
    assert b"devicon-python-plain" in response.data
    assert b"devicon-postgresql-plain" in response.data
    assert b"devicon-scikitlearn-plain" in response.data
    assert response.data.count(b'class="diagram-accent"') == 1
    assert response.data.count(b'<svg viewBox="0 0 48 48"') == 3
    assert response.data.count(b'class="timeline-item"') == 2
    assert b"BISAG-N" in response.data
    assert b"Avisha Association" in response.data
    assert b"University of Leeds" in response.data
    assert b"72.4% overall average" in response.data
    assert b"International Excellence Scholarship" in response.data
    assert b'data-project-universe' in response.data
    assert response.data.count(b'data-universe-node') == 6
    assert response.data.count(b'class="universe-node-dossier"') == 6
    assert response.data.count(b'class="dossier-summary"') == 6
    assert b"Projects built around real problems." in response.data
    assert b"Explore six systems spanning software engineering, data, and applied AI." in response.data
    assert b'<script type="module"' in response.data
    assert b"js/project-universe.js" in response.data
    assert b"js/header-scroll.js" in response.data
    assert b"js/blueprint-reveal.js" in response.data
    assert b"/static/images/favicon.png" in response.data
    assert b'class="identity-mark"' in response.data
    assert b"/static/images/logo.png" in response.data


def test_project_detail(client):
    response = client.get("/projects/scholargraph")

    assert response.status_code == 200
    assert b"ScholarGraph | Aamir Khan" in response.data
    assert b"29 API endpoints" in response.data
    assert b"Project snapshot" in response.data
    assert b"In this case study" in response.data
    assert b"The problem and my part in solving it." in response.data
    assert b'href="#approach"' in response.data
    assert b"32 automated tests" in response.data
    assert b"https://github.com/aamirk24/scholargraph" in response.data
    assert b'href="/projects/nonaga"' in response.data
    assert b'href="/projects/vibecheck"' in response.data


def test_project_without_repository_omits_repository_action(client):
    response = client.get("/projects/repit")

    assert response.status_code == 200
    assert b"View repository" not in response.data
    assert b"1,500 ExerciseDB records" in response.data
    assert b"images/projects/repit-landing.png" in response.data
    assert b"images/projects/repit-dashboard.png" in response.data


def test_flip_uses_product_name_and_case_study_images(client):
    response = client.get("/projects/auction")

    assert response.status_code == 200
    assert b"Flip | Aamir Khan" in response.data
    assert b"Auction Website" not in response.data
    assert b"images/projects/flip-landing.png" in response.data
    assert b"images/projects/flip-product-bidding.png" in response.data


def test_remaining_case_studies_use_reviewed_project_media(client):
    expected_media = {
        "scholargraph": (
            b"images/projects/scholargraph-semantic-search.png",
            b"images/projects/scholargraph-api-overview.png",
        ),
        "nonaga": (
            b"images/projects/nonaga-gameplay.png",
            b"images/projects/nonaga-game-modes.png",
        ),
        "movie-genre-classification": (
            b"images/projects/movie-model-comparison.png",
        ),
        "vibecheck": (
            b"images/projects/vibecheck-results.png",
            b"images/projects/vibecheck-playlist.png",
        ),
    }

    for slug, media_paths in expected_media.items():
        response = client.get(f"/projects/{slug}")

        assert response.status_code == 200
        for media_path in media_paths:
            assert media_path in response.data


def test_project_detail_accepts_trailing_slash(client):
    response = client.get("/projects/scholargraph/")

    assert response.status_code == 200
    assert b"ScholarGraph | Aamir Khan" in response.data


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
    assert b'<meta name="twitter:card" content="summary">' in homepage.data
    assert b'<meta property="og:type" content="article">' in project.data
    assert b"A research platform that connects academic metadata" in project.data


def test_security_and_cache_headers(client):
    page = client.get("/")
    asset = client.get("/static/css/main.css")

    assert "default-src 'self'" in page.headers["Content-Security-Policy"]
    assert page.headers["X-Content-Type-Options"] == "nosniff"
    assert page.headers["X-Frame-Options"] == "DENY"
    assert page.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
    assert page.headers["Cache-Control"] == "no-cache"
    assert asset.headers["Cache-Control"] == "public, max-age=3600, must-revalidate"


def test_search_engine_routes(client):
    robots = client.get("/robots.txt")
    sitemap = client.get("/sitemap.xml")

    assert robots.status_code == 200
    assert robots.mimetype == "text/plain"
    assert b"Allow: /" in robots.data
    assert b"Sitemap: http://localhost/sitemap.xml" in robots.data
    assert sitemap.status_code == 200
    assert sitemap.mimetype == "application/xml"
    assert sitemap.data.count(b"<url>") == 7
    assert b"http://localhost/projects/scholargraph" in sitemap.data


def test_cv_download_is_available(client):
    response = client.get(
        "/static/documents/Aamir_Khan_Software_Engineering_CV.pdf"
    )

    assert response.status_code == 200
    assert response.mimetype == "application/pdf"
    assert response.data.startswith(b"%PDF")


def test_project_universe_script_is_available(client):
    response = client.get("/static/js/project-universe.js")

    assert response.status_code == 200
    assert response.mimetype in {"application/javascript", "text/javascript"}
    assert b"prefers-reduced-motion" in response.data
    assert b"three.module.min.js" in response.data
    assert b"THREE.WebGLRenderer" in response.data
    assert b"Raycaster" in response.data


def test_header_scroll_script_is_available(client):
    response = client.get("/static/js/header-scroll.js")

    assert response.status_code == 200
    assert response.mimetype in {"application/javascript", "text/javascript"}
    assert b"requestAnimationFrame" in response.data
    assert b"is-hidden" in response.data
