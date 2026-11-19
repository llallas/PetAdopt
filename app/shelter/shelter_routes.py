# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_routes.py
# Description: Define the routes for managing shelters

from flask import render_template, request, abort
from app.shelter import shelters_bp
from app.shelter.shelter_controller import ShelterController
from app.shelter.shelter_exceptions import ShelterError


@shelters_bp.route("/", strict_slashes=False)
def list_shelters():
    try:
        # Read the search text and remove surrounding spaces.
        search = request.args.get("search", "").strip()

        shelters = ShelterController.fetch_all_shelters(search)

        # Send the results and search text to the template.
        return render_template(
            "shelters.html",
            shelters=shelters,
            search=search
        )
    except ShelterError:
        raise
    except Exception as e:
        raise ShelterError(
            "Something went wrong while loading the shelters page."
        ) from e

@shelters_bp.route("/<int:shelter_id>")
def shelter_detail(shelter_id):
    # Retrieve the selected shelter and its related pets.
    shelter = ShelterController.fetch_shelter(shelter_id)

    # Show the centralized 404 page when the shelter does not exist.
    if shelter is None:
        abort(404)

    return render_template(
        "shelter_detail.html",
        shelter=shelter
    )