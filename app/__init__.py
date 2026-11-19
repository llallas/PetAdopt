# Author: Elias & Carolyn
# Date: 11/11/2026
# File: __init__.py
# Description: Initialize the Flask application and register blueprints

from flask import Flask, render_template
from database import init_db
from app.errors import register_error_handlers
from app.shelter import shelters_bp
from app.breed import breeds_bp
from app.adopter import adopters_bp
from app.pet.pet_routes import pets_bp

# Register the remaining database models with SQLAlchemy.
from app.pet.pet_model import Pet
from app.application.application_model import Application
from app.vaccination.vaccination_model import Vaccination


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    # Connect and initialize the SQLite database.
    init_db(app)

    # Register domain blueprints.
    app.register_blueprint(shelters_bp)
    app.register_blueprint(breeds_bp)
    app.register_blueprint(adopters_bp)
    app.register_blueprint(pets_bp)

    # Register centralized exception handlers.
    register_error_handlers(app)

    # Display the home page.
    @app.route("/")
    def home():
        return render_template("index.html")

    return app