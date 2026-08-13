from build_static import build_site


def test_static_build_contains_public_site(tmp_path):
    output_directory = build_site(
        output_directory=tmp_path / "dist",
        site_url="https://portfolio.example.com",
    )

    assert (output_directory / "index.html").is_file()
    assert (output_directory / "projects" / "scholargraph" / "index.html").is_file()
    assert (output_directory / "static" / "css" / "main.css").is_file()
    assert (output_directory / "404.html").is_file()
    assert (output_directory / "_headers").is_file()
    assert "https://portfolio.example.com/sitemap.xml" in (
        output_directory / "robots.txt"
    ).read_text()
