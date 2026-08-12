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
        "role": "Individual project",
        "repository_url": "https://github.com/aamirk24/scholargraph",
        "overview": (
            "Academic search often separates paper metadata, citation relationships, "
            "and semantic similarity. ScholarGraph brings those signals together in "
            "one research platform designed for programmatic exploration."
        ),
        "contribution": (
            "I designed and built the platform end to end: its asynchronous API, "
            "relational and vector storage, authentication, ingestion workflows, "
            "scheduled crawling, deployment tooling, and automated tests."
        ),
        "decisions": (
            "Stored 384-dimensional abstract embeddings in PostgreSQL with pgvector so semantic search and relational data could share one persistence layer.",
            "Combined arXiv metadata with Semantic Scholar citation relationships to support both similarity search and graph-based exploration.",
            "Added retry logic with exponential backoff for scheduled ingestion, alongside Alembic migrations, Docker, GitHub Actions, and MCP access for AI clients.",
        ),
        "outcomes": (
            "Delivered 29 FastAPI endpoints covering research, similarity, analytics, authentication, and annotation workflows.",
            "Created 32 automated tests and reached 59% measured test coverage.",
            "Produced a deployed research API that exposes semantic paper discovery and citation intelligence through both REST and MCP interfaces.",
        ),
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
        "role": "Individual dissertation",
        "repository_url": "https://github.com/aamirk24/Nonaga",
        "overview": (
            "Nonaga combines two distinct engineering challenges: creating a useful "
            "computer opponent for a compact strategy game and keeping multiplayer "
            "matches consistent when several clients interact in real time."
        ),
        "contribution": (
            "I built the game as my individual dissertation, covering the rules engine, "
            "fixed-depth adversarial search, heuristic evaluation, browser interface, "
            "server-authoritative multiplayer flow, reconnection, and testing."
        ),
        "decisions": (
            "Used minimax with alpha-beta pruning and three handcrafted heuristics covering token proximity, adjacency, and immediate threats.",
            "Kept match state and action validation on the Flask-SocketIO server rather than trusting individual clients.",
            "Introduced room-based state, reconnect tokens, and a 60-second recovery window to make interrupted matches recoverable.",
        ),
        "outcomes": (
            "Measured the search trade-off at approximately 0.9 seconds for depth 3 and 8 seconds for depth 4.",
            "Created 54 passing pytest tests across eight files.",
            "Received a final dissertation grade of 70% for the 40-credit project.",
        ),
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
        "role": "Individual project",
        "repository_url": None,
        "overview": (
            "RepIT was designed to make workout planning and progress tracking part of "
            "one continuous flow, from saving routines to logging sets during a live "
            "session and reviewing body measurements later."
        ),
        "contribution": (
            "I built the Flask application independently, including authentication, "
            "user-specific routes, the relational schema, routine planning, live workout "
            "logging, exercise data ingestion, and measurement visualisations."
        ),
        "decisions": (
            "Modelled users, exercises, routines, sessions, sets, and measurements with foreign keys and many-to-many SQLAlchemy relationships.",
            "Cached more than 1,500 ExerciseDB records locally and used scheduled refresh jobs to reduce repeated external API requests.",
            "Used Flask-Login, password hashing, and protected routes to keep each user's fitness data separated.",
        ),
        "outcomes": (
            "Delivered saved routines, live session logging, set, repetition, and weight tracking, and body-measurement charts.",
            "Built a reusable local exercise catalogue from more than 1,500 external records.",
            "Demonstrated a complete Flask workflow spanning authentication, relational modelling, external data, and interactive reporting.",
        ),
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
        "role": "Team of six",
        "repository_url": None,
        "overview": (
            "The project brought listings, specialist roles, bidding, payments, and "
            "notifications into a single auction workflow built collaboratively by a "
            "six-person team."
        ),
        "contribution": (
            "I delivered 17 backlog features: 14 independently and three through pair "
            "programming. My work covered listings, search, role-based dashboards, "
            "specialist authentication workflows, responsive UI, and integrations."
        ),
        "decisions": (
            "Used Socket.IO and live countdowns to keep auction activity current without requiring manual page refreshes.",
            "Kept bid validation on the server and used transactional SQLAlchemy updates to protect auction state.",
            "Integrated Stripe test payments and email notifications as part of the end-to-end auction lifecycle.",
        ),
        "outcomes": (
            "Completed 17 backlog features across the team's delivery period.",
            "Combined real-time updates, test payments, notifications, search, and role-based workflows in one responsive application.",
            "Demonstrated both independent delivery and pair-programming contribution within a six-person project.",
        ),
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
        "role": "Individual project",
        "repository_url": None,
        "overview": (
            "This study explored how effectively short movie descriptions can predict "
            "genre when the task is framed as classification across five distinct classes."
        ),
        "contribution": (
            "I collected and prepared the dataset, engineered text features, trained and "
            "compared classifiers, and evaluated performance using both a hold-out split "
            "and cross-validation."
        ),
        "decisions": (
            "Collected 2,500 movie overviews through the TMDB API across five genres.",
            "Engineered keyword, bigram, and trigram features to represent information beyond isolated words.",
            "Compared Naive Bayes, Random Forest, and feature-selected WEKA classifiers using an 80/20 split and 10-fold cross-validation.",
        ),
        "outcomes": (
            "Achieved 66.2% accuracy on the five-class classification task.",
            "Produced a consistent comparison across multiple model families and feature-selection choices.",
            "Developed practical experience with data collection, feature engineering, evaluation design, and multiclass text classification.",
        ),
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
        "role": "Team of two",
        "repository_url": "https://github.com/aamirk24/vibe-check-final",
        "overview": (
            "VibeCheck explored a playful question during a hackathon: could a predicted "
            "facial emotion become a useful starting point for music discovery?"
        ),
        "contribution": (
            "Working in a team of two, I co-created a prototype that connected a "
            "pretrained facial-emotion model with Spotify-based playlist generation."
        ),
        "decisions": (
            "Used a pretrained model so the limited hackathon time could focus on integration and the user journey rather than model training.",
            "Returned confidence scores alongside the emotion prediction to make the model output more transparent.",
            "Connected the predicted mood to Spotify API results to turn an AI inference into an immediate user-facing outcome.",
        ),
        "outcomes": (
            "Produced a working hackathon prototype within the event's time constraints.",
            "Combined computer-vision inference and an external music API in one end-to-end interaction.",
            "Demonstrated rapid collaborative prototyping and integration across distinct services.",
        ),
    },
)


CAPABILITIES = (
    {
        "number": "01",
        "title": "Software engineering",
        "description": (
            "Building tested Python services and full-stack applications with clear "
            "data models, authenticated workflows, and dependable server-side logic."
        ),
        "skills": (
            "Python",
            "Flask",
            "FastAPI",
            "JavaScript",
            "REST APIs",
            "pytest",
        ),
    },
    {
        "number": "02",
        "title": "Data systems",
        "description": (
            "Designing relational schemas and ingestion workflows that turn external "
            "data into structured, searchable, and useful application features."
        ),
        "skills": (
            "SQL",
            "PostgreSQL",
            "SQLAlchemy",
            "pgvector",
            "pandas",
            "Alembic",
        ),
    },
    {
        "number": "03",
        "title": "Applied AI & ML",
        "description": (
            "Applying established models and algorithms with attention to evaluation, "
            "latency, feature design, and the product experience around their outputs."
        ),
        "skills": (
            "scikit-learn",
            "Semantic search",
            "Text classification",
            "PCA",
            "Regression",
            "Minimax",
        ),
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
