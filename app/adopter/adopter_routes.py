# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_routes.py
# Description: Define routes for adopter-related pages and handle exceptions

from flask import render_template
from app.adopter import adopters_bp
from app.adopter.adopter_controller import AdopterController


@adopters_bp.route("/", strict_slashes=False)
def list_adopters():
    # Retrieve adopter records through the controller.
    adopters = AdopterController.fetch_all_adopters()
    return render_template("adopters.html", adopters=adopters)