# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_routes.py
# Description: Define the routes for managing shelters

from flask import Blueprint, render_template
from app.shelter.shelter_manager import ShelterManager
from app.shelter.shelter_exceptions import ShelterDataError

shelters_bp = Blueprint("shelters", __name__, template_folder="templates")

@shelters_bp.route("/shelters")
def list_shelters():
    try:
        shelters = ShelterManager.get_all_shelters()
        return render_template("shelters.html", shelters=shelters)
    except ShelterDataError:
        raise
    except Exception as e:
        raise ShelterDataError("Something went wrong while loading the shelters page.") from e