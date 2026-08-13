from flask import Flask, render_template, request


def create_app(test_config=None):
    """Create and configure the portfolio application."""
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    from app.routes import main

    app.register_blueprint(main)

    @app.after_request
    def apply_response_headers(response):
        """Apply a small, deployment-safe browser security policy."""
        response.headers["Content-Security-Policy"] = "; ".join(
            (
                "default-src 'self'",
                "script-src 'self' https://cdn.jsdelivr.net",
                "style-src 'self' https://cdn.jsdelivr.net https://fonts.googleapis.com",
                "font-src 'self' https://cdn.jsdelivr.net https://fonts.gstatic.com",
                "img-src 'self' data:",
                "connect-src 'self'",
                "object-src 'none'",
                "base-uri 'self'",
                "form-action 'self'",
                "frame-ancestors 'none'",
            )
        )
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=(), payment=()"
        )
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"

        if request.endpoint == "static" and response.status_code == 200:
            response.headers["Cache-Control"] = "public, max-age=3600, must-revalidate"
        elif response.mimetype == "text/html":
            response.headers["Cache-Control"] = "no-cache"

        return response

    @app.errorhandler(404)
    def not_found(error):
        return render_template(
            "error.html",
            error_code="404",
            error_title="Page not found.",
            error_message="The page you’re looking for may have moved or no longer exists.",
        ), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template(
            "error.html",
            error_code="500",
            error_title="Something went wrong.",
            error_message="The site hit an unexpected problem. Please try again shortly.",
        ), 500

    return app
