# Author: Carolyn Rodriguez
# Date: 11/19/26
# File: __init__.py
# Description:

# Define the Pet Blueprint and load its routes.
from flask import Blueprint

pets_bp = Blueprint(
    "pets",
    __name__,
    url_prefix="/pets",
    template_folder="templates"
)

from app.pet import pet_routes