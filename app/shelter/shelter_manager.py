# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_manager.py
# Description: Manage shelter-related operations and interactions with the database

from app.shelter.shelter_model import Shelter
from app.shelter.shelter_exceptions import ShelterDataError

class ShelterManager:
    @staticmethod
    def get_all_shelters():
        try:
            return Shelter.query.all()
        except Exception as e:
            raise ShelterDataError("Could not load shelters from the database.") from e