# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_manager.py
# Description: Manage shelter-related operations and interactions with the database

from sqlalchemy.exc import SQLAlchemyError
from app.shelter.shelter_model import Shelter
from app.shelter.shelter_exceptions import ShelterDatabaseError

class ShelterManager:
    @staticmethod
    def get_all_shelters():
        # Retrieve all shelter records using SQLAlchemy ORM
        try:
            return Shelter.query.all()
        except SQLAlchemyError as e:
            raise ShelterDatabaseError("Failed to retrieve shelters from the database.") from e