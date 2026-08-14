from build_static import build_site
from app.data.projects import FEATURED_PROJECTS


def test_static_build_contains_public_site(tmp_path):
    output_directory = build_site(
        output_directory=tmp_path / "dist",
        site_url="https://portfolio.example.com",
    )

    assert (output_directory / "index.html").is_file()
    for project in FEATURED_PROJECTS:
        assert (
            output_directory / "projects" / project["slug"] / "index.html"
        ).is_file()
    assert (output_directory / "static" / "css" / "main.css").is_file()
    assert (output_directory / "static" / "images" / "favicon.png").is_file()
    assert (output_directory / "static" / "images" / "logo.png").is_file()
    assert (output_directory / "404.html").is_file()
    assert (output_directory / "_headers").is_file()
    assert "https://portfolio.example.com/sitemap.xml" in (
        output_directory / "robots.txt"
    ).read_text()
