# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_manager.py
# Description: Manage adopter-related operations and interactions with the database

from app.adopter.adopter_model import Adopter
from app.adopter.adopter_exceptions import AdopterDataError

class AdopterManager:
    @staticmethod
    def get_all_adopters():
        try:
            return Adopter.query.all()
        except Exception as e:
            raise AdopterDataError("Could not load adopters from the database.") from e