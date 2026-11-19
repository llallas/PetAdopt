# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_routes.py
# Description: Define routes for adopter-related pages and handle exceptions

from flask import abort, render_template, request
from app.adopter import adopters_bp
from app.adopter.adopter_controller import AdopterController
from app.adopter.adopter_exceptions import AdopterNotFoundError


@adopters_bp.route("/", strict_slashes=False)
def list_adopters():
    # Read search and name-sorting query parameters from the request URL
    search_query = request.args.get("search", "")
    match_mode = request.args.get("mode", "all")
    sort_by = request.args.get("sort", "last_name")
    order = request.args.get("order", "asc")

    adopters = AdopterController.fetch_adopters(
        search_query=search_query,
        match_mode=match_mode,
        sort_by=sort_by,
        order=order,
    )

    return render_template(
        "adopters.html",
        adopters=adopters,
        search_query=search_query,
        match_mode=match_mode,
        selected_sort=sort_by,
        selected_order=order,
    )


@adopters_bp.route("/<int:adopter_id>")
def adopter_detail(adopter_id):
    # Display adopter details and all submitted adoption applications
    try:
        adopter = AdopterController.fetch_adopter_details(adopter_id)
    except AdopterNotFoundError:
        abort(404)
    return render_template("adopter_detail.html", adopter=adopter)