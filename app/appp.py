# Flask modules
from flask import Flask

# Other modules
import os


def create_app(debug: bool = False):

    # Create the Flask application instance
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
        static_url_path="/",
    )
    return app