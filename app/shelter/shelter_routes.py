# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_routes.py
# Description: Define the routes for managing shelters

from flask import render_template
from app.shelter import shelters_bp
from app.shelter.shelter_controller import ShelterController

@shelters_bp.route("/", strict_slashes=False)
def list_shelters():
    # Retrieve shelter records through the controller.
    shelters = ShelterController.fetch_all_shelters()
    return render_template("shelters.html", shelters=shelters)