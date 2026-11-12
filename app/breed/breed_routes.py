# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_routes.py
# Description: Define the routes for breed-related pages in the Flask application
from flask import Blueprint, render_template
from app.breed.breed_manager import BreedManager
from app.breed.breed_exceptions import BreedDataError

breeds_bp = Blueprint("breeds", __name__, template_folder="templates")

@breeds_bp.route("/breeds")
def list_breeds():
    try:
        breeds = BreedManager.get_all_breeds()
        return render_template("breeds.html", breeds=breeds)
    except BreedDataError:
        raise
    except Exception as e:
        raise BreedDataError("Something went wrong while loading the breeds page.") from e