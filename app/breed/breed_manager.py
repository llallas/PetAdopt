# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_manager.py
# Description: Manage breed-related operations and interactions with the database

from app.breed.breed_model import Breed
from app.breed.breed_exceptions import BreedDataError

class BreedManager:
    @staticmethod
    def get_all_breeds():
        try:
            return Breed.query.all()
        except Exception as e:
            raise BreedDataError("Could not load breeds from the database.") from e