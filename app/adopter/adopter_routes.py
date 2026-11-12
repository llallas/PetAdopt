# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_routes.py
# Description: Define routes for adopter-related pages and handle exceptions

from flask import Blueprint, render_template
from app.adopter.adopter_manager import AdopterManager
from app.adopter.adopter_exceptions import AdopterDataError

adopters_bp = Blueprint("adopters", __name__, template_folder="templates")

@adopters_bp.route("/adopters")
def list_adopters():
    try:
        adopters = AdopterManager.get_all_adopters()
        return render_template("adopters.html", adopters=adopters)
    except AdopterDataError:
        raise
    except Exception as e:
        raise AdopterDataError("Something went wrong while loading the adopters page.") from e