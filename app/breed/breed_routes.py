# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_routes.py
# Description: Define the routes for breed-related pages in the Flask application
from flask import Blueprint, render_template
from app.breed.breed_controller import BreedController

# Create the breed blueprint with URL prefix /breeds
breeds_bp = Blueprint("breeds", __name__, url_prefix="/breeds")

@breeds_bp.route("/", strict_slashes=False)
def list_breeds():
    # Fetch all breeds via the controller and render the template
    breeds = BreedController.fetch_all_breeds()
    return render_template("breeds.html", breeds=breeds)