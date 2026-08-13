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
    assert b"Auction Website" in response.data
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


def test_project_detail(client):
    response = client.get("/projects/scholargraph")

    assert response.status_code == 200
    assert b"ScholarGraph | Aamir Khan" in response.data
    assert b"29 API endpoints" in response.data
    assert b"What the project set out to do." in response.data
    assert b"My role in the work." in response.data
    assert b"32 automated tests" in response.data
    assert b"https://github.com/aamirk24/scholargraph" in response.data
    assert b'href="/projects/nonaga"' in response.data
    assert b'href="/projects/vibecheck"' in response.data


def test_project_without_repository_omits_repository_action(client):
    response = client.get("/projects/repit")

    assert response.status_code == 200
    assert b"View repository" not in response.data
    assert b"1,500 ExerciseDB records" in response.data


def test_unknown_project_returns_not_found(client):
    response = client.get("/projects/unknown-project")

    assert response.status_code == 404


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
    assert b"three.module.js" in response.data
    assert b"THREE.WebGLRenderer" in response.data
    assert b"Raycaster" in response.data


def test_header_scroll_script_is_available(client):
    response = client.get("/static/js/header-scroll.js")

    assert response.status_code == 200
    assert response.mimetype in {"application/javascript", "text/javascript"}
    assert b"requestAnimationFrame" in response.data
    assert b"is-hidden" in response.data
