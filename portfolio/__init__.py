from flask import Flask


def create_app(test_config=None):
    """Create and configure the portfolio application."""
    app = Flask(__name__)

    if test_config is not None:
        app.config.from_mapping(test_config)

    from portfolio.routes import main

    app.register_blueprint(main)

    return app
