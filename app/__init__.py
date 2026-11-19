# Author: Elias & Carolyn
# Date: 11/11/2026
# File: __init__.py
# Description: Initialize the Flask application and register blueprints

from flask import Flask, render_template
from database import init_db
from app.errors import register_error_handlers
from app.shelter.shelter_routes import shelters_bp
from app.breed.breed_routes import breeds_bp
from app.adopter.adopter_routes import adopters_bp

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    # Connect and initialize the SQLite database
    init_db(app)

    # Register domain blueprints
    app.register_blueprint(shelters_bp)
    app.register_blueprint(breeds_bp)
    app.register_blueprint(adopters_bp)

    # Register centralized exception handlers
    register_error_handlers(app)

    # Home route
    @app.route("/")
    def home():
        return render_template("index.html")

    return app