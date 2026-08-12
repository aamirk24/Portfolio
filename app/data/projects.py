FEATURED_PROJECTS = (
    {
        "slug": "scholargraph",
        "title": "ScholarGraph",
        "category": "Software / Data / AI",
        "year": "2026",
        "summary": (
            "A research platform that connects academic metadata, citation graphs, "
            "and semantic embeddings to make relevant papers easier to discover."
        ),
        "highlight": "29 API endpoints",
        "technologies": ("FastAPI", "PostgreSQL", "pgvector", "Docker"),
        "visual": "network",
    },
    {
        "slug": "nonaga",
        "title": "Nonaga",
        "category": "Software / Algorithms",
        "year": "2026",
        "summary": (
            "A server-authoritative multiplayer strategy game with a minimax opponent, "
            "real-time rooms, and resilient player reconnection."
        ),
        "highlight": "54 passing tests",
        "technologies": ("Python", "Flask", "Socket.IO", "pytest"),
        "visual": "board",
    },
    {
        "slug": "repit",
        "title": "RepIT",
        "category": "Full-stack software",
        "year": "2025",
        "summary": (
            "A workout platform for building routines, logging live sessions, and "
            "tracking body measurements through a relational data model."
        ),
        "highlight": "1,500+ exercises cached",
        "technologies": ("Flask", "SQLAlchemy", "JavaScript", "Chart.js"),
        "visual": "rings",
    },
    {
        "slug": "auction",
        "title": "Auction Website",
        "category": "Team software project",
        "year": "2025",
        "summary": (
            "A real-time auction system with role-based workflows, live bidding, "
            "test payments, notifications, and server-side bid validation."
        ),
        "highlight": "17 backlog features",
        "technologies": ("Flask", "SQLAlchemy", "Socket.IO", "Stripe"),
        "visual": "pulse",
    },
    {
        "slug": "movie-genre-classification",
        "title": "Movie Genre Classification",
        "category": "Applied machine learning",
        "year": "2025",
        "summary": (
            "A five-class text-classification study comparing multiple models and "
            "engineered language features from movie overviews."
        ),
        "highlight": "2,500 overviews analysed",
        "technologies": ("Python", "TMDB API", "WEKA", "scikit-learn"),
        "visual": "frames",
    },
    {
        "slug": "vibecheck",
        "title": "VibeCheck",
        "category": "Hackathon / Applied AI",
        "year": "2025",
        "summary": (
            "A hackathon prototype pairing facial-emotion predictions with Spotify "
            "to generate mood-aligned playlists and confidence scores."
        ),
        "highlight": "Team of two",
        "technologies": ("Python", "Flask", "Spotify API", "Machine learning"),
        "visual": "wave",
    },
)


def get_project(slug):
    """Return a project matching the supplied slug, if one exists."""
    return next(
        (project for project in FEATURED_PROJECTS if project["slug"] == slug),
        None,
    )


def get_adjacent_projects(slug):
    """Return the projects immediately before and after the supplied project."""
    project_index = next(
        (
            index
            for index, project in enumerate(FEATURED_PROJECTS)
            if project["slug"] == slug
        ),
        None,
    )

    if project_index is None:
        return None, None

    previous_project = FEATURED_PROJECTS[project_index - 1]
    next_project = FEATURED_PROJECTS[(project_index + 1) % len(FEATURED_PROJECTS)]

    return previous_project, next_project
