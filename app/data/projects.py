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
        "highlight": "29 endpoints · 32 tests",
        "technologies": ("FastAPI", "PostgreSQL", "pgvector", "Docker"),
        "role": "Individual project",
        "repository_url": "https://github.com/aamirk24/scholargraph",
        "hero_image": "images/projects/scholargraph-semantic-search.png",
        "hero_image_alt": "ScholarGraph semantic-search API response with ranked academic papers",
        "hero_image_caption": "Semantic retrieval results ranked against a natural-language research query.",
        "secondary_image": "images/projects/scholargraph-api-overview.png",
        "secondary_image_alt": "ScholarGraph interactive API documentation showing its endpoint groups",
        "secondary_image_caption": "The documented API surface across authentication, crawling, papers, annotations, and analytics.",
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
        "highlight": "70% dissertation · 54 tests",
        "technologies": ("Python", "Flask", "Socket.IO", "pytest"),
        "role": "Individual dissertation",
        "repository_url": "https://github.com/aamirk24/Nonaga",
        "hero_image": "images/projects/nonaga-gameplay.png",
        "hero_image_alt": "Nonaga strategy board during a game against the computer",
        "hero_image_caption": "A live match against the minimax opponent, with legal moves surfaced directly on the board.",
        "secondary_image": "images/projects/nonaga-game-modes.png",
        "secondary_image_alt": "Nonaga mode selection for local, computer, and online multiplayer",
        "secondary_image_caption": "One rules engine presented through local, computer, and real-time online play.",
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
        "category": "Full-stack / Data",
        "year": "2025",
        "summary": (
            "A production-deployed strength-training platform for planning routines, "
            "recording recoverable workouts, and analysing long-term progress."
        ),
        "highlight": "Live product · 35 tests",
        "technologies": ("Flask", "PostgreSQL", "SQLAlchemy", "Chart.js"),
        "role": "Individual project",
        "repository_url": "https://github.com/aamirk24/RepIT",
        "live_url": "https://repit-inq2.onrender.com/",
        "hero_image": "images/projects/repit-workout-tracking.png",
        "hero_image_alt": "RepIT active workout showing a recoverable timer, session details, exercises, and editable sets",
        "hero_image_caption": "A recoverable live session keeps workout context, exercise order, repetitions, load, and rest data together.",
        "secondary_image": "images/projects/repit-progress.png",
        "secondary_image_alt": "RepIT progress dashboard showing training totals, consistency, personal records, and estimated one-repetition maximum",
        "secondary_image_caption": "Completed sets become consistency, volume, personal-record, and estimated 1RM insights.",
        "overview": (
            "RepIT connects routine planning, active workout tracking, immutable history, "
            "strength analytics, and body measurements rather than treating them as "
            "separate tools. It began as a university Flask project and was rebuilt into "
            "a deployed product with explicit data-integrity and operational boundaries."
        ),
        "contribution": (
            "I independently rebuilt the application across its Flask services, relational "
            "model, authentication, recoverable workout lifecycle, catalogue synchronisation, "
            "analytics, responsive interface, automated checks, and production deployment."
        ),
        "decisions": (
            "Made active workouts recoverable and completed workouts immutable, with transaction-safe services and database constraints protecting ownership, ordering, and valid set values.",
            "Replaced the retired paid API dependency with a checksum-verified snapshot of 873 Free Exercise DB records, while snapshotting exercise identity into completed history.",
            "Kept kilograms and centimetres as canonical storage while providing metric and imperial presentation, defensible volume and estimated 1RM calculations, and accessible alternatives to charts.",
        ),
        "outcomes": (
            "Deployed the application through Render and Neon PostgreSQL with migrations, health checks, structured logging, security headers, and concurrency-safe startup preparation.",
            "Delivered reusable routines, resumable live sessions, immutable workout history, measurement tracking, personal records, streaks, volume, and estimated 1RM trends.",
            "Created 35 passing automated tests alongside migration, compilation, and dependency-audit checks in GitHub Actions.",
        ),
    },
    {
        "slug": "flip",
        "title": "Flip",
        "category": "Team software project",
        "year": "2025",
        "summary": (
            "A real-time auction system with role-based workflows, live bidding, "
            "test payments, notifications, and server-side bid validation."
        ),
        "highlight": "17 backlog features delivered",
        "technologies": ("Flask", "SQLAlchemy", "Socket.IO", "Stripe"),
        "role": "Team of six",
        "repository_url": None,
        "hero_image": "images/projects/flip-landing.png",
        "hero_image_alt": "Flip fashion-auction landing page",
        "hero_image_caption": "Flip’s fashion-led landing experience introduces the auction platform’s visual identity.",
        "secondary_image": "images/projects/flip-product-bidding.png",
        "secondary_image_alt": "Flip product page showing live auction details and the bidding interface",
        "secondary_image_caption": "The product workflow combines live pricing, countdown state, watchlists, and bid entry.",
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
        "highlight": "66.2% accuracy · 2,500 overviews",
        "technologies": ("Python", "TMDB API", "WEKA", "scikit-learn"),
        "role": "Individual project",
        "repository_url": None,
        "hero_image": "images/projects/movie-model-comparison.png",
        "hero_image_alt": "Comparison of four movie genre classification models and their measured accuracy",
        "hero_image_caption": "Ten-fold cross-validation results across four classifiers trained on 2,500 movie overviews.",
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
            "A two-person hackathon prototype that classifies a visible facial expression "
            "with a pretrained model and matches its label to a Spotify playlist."
        ),
        "highlight": "Two-day build · 18 tests",
        "technologies": ("Flask", "Hugging Face", "PyTorch", "Spotify API"),
        "role": "Two-person hackathon team",
        "repository_url": "https://github.com/aamirk24/vibe-check",
        "hero_image": "images/projects/vibecheck-results.png",
        "hero_image_alt": "VibeCheck facial-expression prediction with a confidence score and Spotify recommendation",
        "hero_image_caption": "A predicted expression label, confidence score, and playlist recommendation in one result flow.",
        "overview": (
            "Built during the two-day Encode Vibe Coding Hackathon in London, VibeCheck "
            "explored how existing AI and music services could become a playful web "
            "experience under tight delivery constraints."
        ),
        "contribution": (
            "Working in a team of two, I co-created the Flask prototype connecting webcam "
            "capture, pretrained Hugging Face inference, Spotify search and playback, "
            "confidence reporting, and optional corrective-feedback logging."
        ),
        "decisions": (
            "Used the pretrained dima806 facial-expression classifier without claiming model training, fine-tuning, or ownership, keeping the work focused on integration and user experience.",
            "Described outputs as visible facial-expression predictions rather than reliable measurements of internal mood, and surfaced both confidence and corrective feedback.",
            "Mapped predicted labels to Spotify search phrases, embedded the first matching playlist, and made Comet ML logging optional with an explicit privacy notice.",
        ),
        "outcomes": (
            "Produced a complete webcam-to-playlist interaction during a two-day collaborative hackathon.",
            "Added 18 isolated automated tests and GitHub Actions without requiring model downloads, credentials, or external network calls.",
            "Improved the prototype with accessible feedback states, clearer privacy wording, safer request handling, and in-memory Spotify token caching.",
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
            {"name": "Python", "icon": "devicon-python-plain"},
            {"name": "Flask", "icon": "devicon-flask-original"},
            {"name": "FastAPI", "icon": "devicon-fastapi-plain"},
            {"name": "JavaScript", "icon": "devicon-javascript-plain"},
            {"name": "pytest", "icon": "devicon-pytest-plain"},
            {"name": "REST APIs", "symbol": "</>"},
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
            {"name": "PostgreSQL", "icon": "devicon-postgresql-plain"},
            {"name": "MySQL", "icon": "devicon-mysql-original"},
            {"name": "SQLAlchemy", "icon": "devicon-sqlalchemy-plain"},
            {"name": "pandas", "icon": "devicon-pandas-plain"},
            {"name": "Docker", "icon": "devicon-docker-plain"},
            {"name": "pgvector", "symbol": "[v]"},
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
            {"name": "scikit-learn", "icon": "devicon-scikitlearn-plain"},
            {"name": "Python", "icon": "devicon-python-plain"},
            {"name": "Semantic search", "diagram": "semantic-search"},
            {"name": "Text classification", "symbol": "Aa"},
            {"name": "PCA / Regression", "diagram": "regression"},
            {"name": "Minimax", "diagram": "minimax"},
        ),
    },
)


EXPERIENCE = (
    {
        "period": "Jun - Aug 2024",
        "organisation": "BISAG-N",
        "location": "New Delhi",
        "role": "Python Developer Intern",
        "summary": (
            "Worked in a professional technology environment, strengthened Python "
            "skills through structured independent practice, and served as a rapporteur "
            "at the Global India AI Summit."
        ),
        "detail": (
            "Produced a concise internal summary of talks and discussions from senior "
            "technology leaders."
        ),
    },
    {
        "period": "Jul - Sep 2023",
        "organisation": "Avisha Association",
        "location": "Noida",
        "role": "Technical Volunteer",
        "summary": (
            "Independently built a Python and MySQL desktop application for the NGO's "
            "local office."
        ),
        "detail": (
            "Enabled the owner to create, edit, delete, and search operational water-pot "
            "records."
        ),
    },
)


EDUCATION = {
    "period": "Sep 2023 - Jul 2026",
    "institution": "University of Leeds",
    "qualification": "BSc Computer Science, First-Class Honours",
    "average": "72.4% overall average",
    "highlights": (
        "Web Application Development - 96%",
        "Object-Oriented Programming - 86%",
        "Machine Learning - 80%",
        "Software Engineering Principles - 80%",
    ),
    "scholarship": (
        "International Excellence Scholarship recipient, receiving £5,000 across the "
        "degree through continuation awards based on academic performance."
    ),
}


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
