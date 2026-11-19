# Author: Elias Arriaga
# Date: 11/11/2026
# File: __init__.py
# Description: Marks the breed directory as a Python package.

# Define the Breed Blueprint and load its routes.
from flask import Blueprint

breeds_bp = Blueprint(
    "breeds",
    __name__,
    url_prefix="/breeds",
    template_folder="templates"
)

from app.breed import breed_routes