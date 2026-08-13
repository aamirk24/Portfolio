# Aamir Khan - Portfolio

A recruiter-facing portfolio presenting my work across software engineering, data systems, and applied AI.

![Portfolio homepage](docs/assets/portfolio-homepage.jpg)

## Overview

This portfolio is a server-rendered Flask application. It combines a clean editorial interface with a Three.js Project Universe that turns six selected projects into an interactive, spatial navigation experience.

## Highlights

- Kinetic introduction spanning software engineering, data systems, and applied AI
- Interactive 3D Project Universe with keyboard, pointer, and touch support
- Six data-driven project case studies with reusable routing and templates
- Responsive layouts for desktop, tablet, and mobile
- Reduced-motion and non-WebGL fallbacks
- Downloadable CV
- Contextual metadata, sitemap, crawler guidance, and custom error pages
- Browser security and asset-caching policies
- Automated route, navigation, metadata, and content-structure tests

## Project Universe

![Interactive Project Universe](docs/assets/portfolio-project-universe.jpg)

The universe provides direct access to the selected projects.

Each node reveals a concise dossier before opening the complete case study. The interaction progressively enhances standard links, so the projects remain navigable when WebGL or JavaScript is unavailable.

## Technology

| Area | Technology |
| --- | --- |
| Application | Python, Flask, Jinja |
| Interface | HTML, CSS, Bootstrap, JavaScript |
| 3D experience | Three.js |
| Testing | pytest |

Browser dependencies are loaded explicitly through CDN links, with Bootstrap, Three.js, and Devicon pinned to fixed versions. The application itself requires only Flask at runtime.

## Structure

```text
app/
├── data/                 Structured portfolio and project content
├── static/
│   ├── css/              Visual system and responsive layouts
│   ├── documents/        Downloadable CV
│   └── js/               Header, hero, and Project Universe behaviour
├── templates/            Homepage, case studies, errors, and sitemap
├── __init__.py           Application factory and response policies
└── routes.py             Homepage, project, and discovery routes
tests/                    Application and content-contract tests
```

## Contact

- [GitHub](https://github.com/aamirk24)
- [LinkedIn](https://www.linkedin.com/in/aamirkhan05/)
- [aamirk2405@gmail.com](mailto:aamirk2405@gmail.com)
