# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_routes.py
# Description: Define the routes for breed-related pages in the Flask application

from flask import abort, render_template
from app.breed import breeds_bp
from app.breed.breed_controller import BreedController


@breeds_bp.route("/", strict_slashes=False)
def list_breeds():
    # Retrieve breed records through the controller.
    breeds = BreedController.fetch_all_breeds()
    return render_template("breeds.html", breeds=breeds)


@breeds_bp.route("/<int:breed_id>")
def breed_detail(breed_id):
    # Retrieve one breed through the controller.
    breed = BreedController.fetch_breed_details(breed_id)
    if breed is None:
        abort(404)
    return render_template("breed_detail.html", breed=breed)