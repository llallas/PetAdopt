# Author: Elias Arriaga
# Date: 11/18/2026
# File: pet_routes.py
# Description: Defines Blueprint routes for listing/filtering pets and viewing pet details.

from flask import Blueprint, render_template, request, abort
from app.pet.pet_controller import PetController
from app.breed.breed_controller import BreedController
from app.pet.pet_exceptions import PetNotFoundError

pets_bp = Blueprint("pets", __name__, url_prefix="/pets")


@pets_bp.route("/", strict_slashes=False)
def list_pets():
    # Read filter, sort, and limit query parameters from the request URL
    breed_id_raw = request.args.get("breed_id", "")
    sex = request.args.get("sex", "")
    spay_neuter = request.args.get("spay_neuter", "")
    sort_by = request.args.get("sort", "name")
    order = request.args.get("order", "asc")
    limit_raw = request.args.get("limit", "")

    # Fetch filtered pets and all breeds (to populate the breed dropdown)
    pets = PetController.fetch_pets(
        breed_id_raw=breed_id_raw,
        sex=sex,
        spay_neuter=spay_neuter,
        sort_by=sort_by,
        order=order,
        limit_raw=limit_raw,
    )
    breeds = BreedController.fetch_breeds()

    # Convert selected breed_id to int if valid so the dropdown keeps it selected
    selected_breed_id = int(breed_id_raw) if breed_id_raw.isdigit() else None

    return render_template(
        "pets.html",
        pets=pets,
        breeds=breeds,
        selected_breed_id=selected_breed_id,
        selected_sex=sex,
        selected_spay_neuter=spay_neuter,
        selected_sort=sort_by,
        selected_order=order,
        limit_value=limit_raw,
    )


@pets_bp.route("/<int:pet_id>")
def pet_detail(pet_id):
    # Render a single pet page with related shelter, breed, vaccination, and application data
    try:
        pet = PetController.fetch_pet_details(pet_id)
    except PetNotFoundError:
        abort(404)
    return render_template("pet_detail.html", pet=pet)