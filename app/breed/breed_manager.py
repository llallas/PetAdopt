# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_manager.py
# Description: Manage breed-related operations and interactions with the database

from sqlalchemy.exc import SQLAlchemyError
from app.breed.breed_model import Breed
from app.breed.breed_exceptions import BreedDatabaseError

class BreedManager:
    @staticmethod
    def get_all_breeds():
        # Retrieve all breed records using SQLAlchemy ORM
        try:
            return Breed.query.all()
        except SQLAlchemyError as e:
            raise BreedDatabaseError("Failed to retrieve breeds from the database.") from e
