# Author: Elias Arriaga
# Date: 11/18/2026
# File: pet_controller.py
# Description: Controller validating query parameters and managing pet application logic.

from app.pet.pet_manager import PetManager
from app.pet.pet_exceptions import (
    PetError,
    PetValidationError,
    PetNotFoundError,
)


class PetController:
    @staticmethod
    def fetch_pets(
        breed_id_raw="",
        sex="",
        spay_neuter="",
        sort_by="name",
        order="asc",
        limit_raw="",
    ):
        # Validate query parameters before passing them to the manager
        try:
            # Validate breed_id parameter if selected
            breed_id = None
            if breed_id_raw:
                try:
                    breed_id = int(breed_id_raw)
                except ValueError as e:
                    raise PetValidationError("Breed ID must be a valid whole number.") from e
                if breed_id <= 0:
                    raise PetValidationError("Breed ID must be greater than 0.")

            # Validate sort field and sort direction
            if sort_by not in PetManager.SORT_FIELDS:
                raise PetValidationError(f"Invalid sort field: '{sort_by}'.")

            if order not in ("asc", "desc"):
                raise PetValidationError("Sort order must be 'asc' or 'desc'.")

            # Validate limit parameter if provided
            limit = None
            if limit_raw:
                try:
                    limit = int(limit_raw)
                except ValueError as e:
                    raise PetValidationError("Limit must be a positive whole number.") from e
                if limit <= 0:
                    raise PetValidationError("Limit must be greater than 0.")

            return PetManager.get_filtered_pets(
                breed_id=breed_id,
                sex=sex.strip() or None,
                spay_neuter=spay_neuter.strip() or None,
                sort_by=sort_by,
                order=order,
                limit=limit,
            )
        except PetError:
            raise
        except Exception as e:
            raise PetError("An unexpected error occurred while filtering pets.") from e

    @staticmethod
    def fetch_pet_details(pet_id):
        # Fetch a pet and ensure its related records can be loaded
        try:
            pet = PetManager.get_pet_by_id(pet_id)
            if pet is None:
                raise PetNotFoundError(f"Pet with ID {pet_id} was not found.")

            # Access ORM relationships so any loading errors are caught here
            _ = pet.shelter
            _ = pet.breed
            _ = pet.vaccinations
            _ = pet.applications

            return pet
        except PetError:
            raise
        except Exception as e:
            raise PetError("An error occurred while loading related pet details.") from e