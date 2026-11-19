# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_manager.py
# Description: Manage adopter-related operations and interactions with the database

from sqlalchemy.exc import SQLAlchemyError
from app.adopter.adopter_model import Adopter
from app.adopter.adopter_exceptions import AdopterDatabaseError

class AdopterManager:
    @staticmethod
    def get_all_adopters():
        # Retrieve all adopter records using SQLAlchemy ORM
        try:
            return Adopter.query.all()
        except SQLAlchemyError as e:
            raise AdopterDatabaseError("Failed to retrieve adopters from the database.") from e