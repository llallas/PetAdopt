# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_manager.py
# Description: Manage shelter-related operations and interactions with the database

from sqlalchemy.exc import SQLAlchemyError
from app.shelter.shelter_model import Shelter
from app.shelter.shelter_exceptions import ShelterDatabaseError
from sqlalchemy.orm import selectinload


class ShelterManager:
    @staticmethod
    def get_all_shelters(search=""):
        # Retrieve shelter records using SQLAlchemy ORM.
        try:
            query = Shelter.query

            # Require each search word to appear in the shelter name.
            for term in search.split():
                query = query.filter(
                    Shelter.name.like("%" + term + "%")
                )

            return query.all()
        except SQLAlchemyError as e:
            raise ShelterDatabaseError(
                "Failed to retrieve shelters from the database."
            ) from e

    @staticmethod
    def get_shelter(shelter_id):
        # Load the shelter and its related pets within the error handling.
        try:
            return Shelter.query.options(
                selectinload(Shelter.pets)
            ).filter(
                Shelter.shelter_id == shelter_id
            ).first()
        except SQLAlchemyError as e:
            raise ShelterDatabaseError(
                "Failed to retrieve the shelter and its pets."
            ) from e