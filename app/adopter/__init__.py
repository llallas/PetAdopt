# Author: Elias Arriaga
# Date: 11/11/2026
# File: __init__.py
# Description: Marks the breed directory as a Python package.

# Define the Adopter Blueprint and load its routes.
from flask import Blueprint

adopters_bp = Blueprint(
    "adopters",
    __name__,
    url_prefix="/adopters",
    template_folder="templates"
)

from app.adopter import adopter_routes