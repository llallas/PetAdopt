# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_routes.py
# Description: Define the routes for breed-related pages in the Flask application

from flask import render_template
from app.breed import breeds_bp
from app.breed.breed_controller import BreedController


@breeds_bp.route("/", strict_slashes=False)
def list_breeds():
    # Retrieve breed records through the controller.
    breeds = BreedController.fetch_all_breeds()
    return render_template("breeds.html", breeds=breeds)