# Author: Elias Arriaga
# Date: 11/18/2026
# File: pet_manager.py
# Description:Data access layer for querying and filtering pet records from the database.

from sqlalchemy.exc import SQLAlchemyError
from app.pet.pet_model import Pet
from app.pet.pet_exceptions import PetDatabaseError


class PetManager:
    # Map allowed sort query values to Pet model columns
    SORT_FIELDS = {
        "name": Pet.name,
        "intake_date": Pet.intake_date,
        "birth_date": Pet.birth_date,
    }

    @staticmethod
    def get_filtered_pets(
        breed_id=None,
        sex=None,
        spay_neuter=None,
        sort_by="name",
        order="asc",
        limit=None,
    ):
        # Build SQLAlchemy query with optional breed, sex, spay/neuter filters, sorting, and limit
        try:
            query = Pet.query

            # Filter by breed foreign key when a valid breed_id is provided
            if breed_id is not None:
                query = query.filter(Pet.breed_id == breed_id)

            # Apply additional optional attribute filters
            if sex:
                query = query.filter(Pet.sex == sex)
            if spay_neuter:
                query = query.filter(Pet.spay_neuter_status == spay_neuter)

            # Apply ascending or descending sorting
            sort_column = PetManager.SORT_FIELDS.get(sort_by, Pet.name)
            if order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())

            # Apply result limit if provided
            if limit is not None:
                query = query.limit(limit)

            return query.all()
        except SQLAlchemyError as e:
            raise PetDatabaseError("Failed to retrieve filtered pets from the database.") from e

    @staticmethod
    def get_pet_by_id(pet_id):
        # Retrieve a single pet record by primary key
        try:
            return Pet.query.get(pet_id)
        except SQLAlchemyError as e:
            raise PetDatabaseError("Failed to retrieve pet details from the database.") from e