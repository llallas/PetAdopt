# Author: Elias Arriaga
# Date: 11/11/2026
# File: __init__.py
# Description: Marks the shelter directory as a Python package.

# Define the Shelter Blueprint and load its routes.
from flask import Blueprint

shelters_bp = Blueprint(
    "shelters",
    __name__,
    url_prefix="/shelters",
    template_folder="templates"
)

from app.shelter import shelter_routes