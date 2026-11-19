# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_routes.py
# Description: Define routes for adopter-related pages and handle exceptions

from flask import Blueprint, render_template
from app.adopter.adopter_controller import AdopterController

# Create the adopter blueprint with URL prefix /adopters
adopters_bp = Blueprint("adopters", __name__, url_prefix="/adopters")

@adopters_bp.route("/", strict_slashes=False)
def list_adopters():
    # Fetch all adopters via the controller and render the template
    adopters = AdopterController.fetch_all_adopters()
    return render_template("adopters.html", adopters=adopters)