# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_routes.py
# Description: Define the routes for managing shelters

from flask import Blueprint, render_template
from app.shelter.shelter_controller import ShelterController

# Create the shelter blueprint with URL prefix /shelters
shelters_bp = Blueprint("shelters", __name__, url_prefix="/shelters")

@shelters_bp.route("/", strict_slashes=False)
def list_shelters():
    # Fetch all shelters via the controller and render the template
    shelters = ShelterController.fetch_all_shelters()
    return render_template("shelters.html", shelters=shelters)