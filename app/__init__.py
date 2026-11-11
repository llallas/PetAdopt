# Author: Elias & Carolyn
# Date: 11/11/2026
# File: __init__.py
# Description: Initialize the Flask application and register blueprints

from flask import Flask, render_template
from database import init_db
from app.shelter.shelter_routes import shelters_bp
from app.breed.breed_routes import breeds_bp
from app.adopter.adopter_routes import adopters_bp

from app.shelter.shelter_exceptions import ShelterDataError
from app.breed.breed_exceptions import BreedDataError
from app.adopter.adopter_exceptions import AdopterDataError

def create_app():
    app = Flask(__name__)
    init_db(app)

    app.register_blueprint(shelters_bp)
    app.register_blueprint(breeds_bp)
    app.register_blueprint(adopters_bp)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.errorhandler(ShelterDataError)
    @app.errorhandler(BreedDataError)
    @app.errorhandler(AdopterDataError)
    def handle_domain_error(error):
        return render_template("error.html", message=str(error)), 500

    @app.errorhandler(404)
    def handle_not_found(error):
        return render_template("error.html", message="Page not found."), 404

    return app