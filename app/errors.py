# Author: Elias Arriaga
# Date: 11/18/2026
# File: errors.py
# Centralized exception handling for domain errors, database errors, and HTTP errors.

from flask import render_template
from sqlalchemy.exc import SQLAlchemyError
from app.shelter.shelter_exceptions import ShelterError
from app.breed.breed_exceptions import BreedError
from app.adopter.adopter_exceptions import AdopterError, AdopterValidationError
from app.pet.pet_exceptions import PetError, PetValidationError


def register_error_handlers(app):
    # Return 400 when search or filter inputs are invalid.
    @app.errorhandler(AdopterValidationError)
    @app.errorhandler(PetValidationError)
    def handle_validation_error(error):
        return render_template("error.html", message=str(error)), 400

    # Handle custom exceptions raised by any domain.
    @app.errorhandler(ShelterError)
    @app.errorhandler(BreedError)
    @app.errorhandler(AdopterError)
    @app.errorhandler(PetError)
    def handle_domain_error(error):
        return render_template("error.html", message=str(error)), 500

    # Catch any unhandled SQLAlchemy database errors.
    @app.errorhandler(SQLAlchemyError)
    def handle_database_error(error):
        return render_template(
            "error.html",
            message="A database error occurred while retrieving data."
        ), 500

    # Handle 404 Page Not Found errors.
    @app.errorhandler(404)
    def handle_not_found(error):
        return render_template(
            "error.html",
            message="The requested page could not be found."
        ), 404

    # Handle unexpected 500 server errors.
    @app.errorhandler(500)
    def handle_internal_error(error):
        return render_template(
            "error.html",
            message="An unexpected server error occurred."
        ), 500