# Author: Elias Arriaga
# Date: 11/18/2026
# File: adopter_controller.py
# Description: Controller handling application logic between adopter routes and the adopter manager.

from app.adopter.adopter_manager import AdopterManager
from app.adopter.adopter_exceptions import (
    AdopterError,
    AdopterValidationError,
    AdopterNotFoundError,
)


class AdopterController:
    @staticmethod
    def fetch_adopters(search_query="", match_mode="all", sort_by="last_name", order="asc"):
        # Validate sort field, sort direction, and search match mode before querying
        try:
            if sort_by not in AdopterManager.SORT_FIELDS:
                raise AdopterValidationError(
                    f"Invalid sort field '{sort_by}'. Use 'first_name' or 'last_name'."
                )

            if order not in ("asc", "desc"):
                raise AdopterValidationError("Sort order must be 'asc' or 'desc'.")

            if match_mode not in ("all", "any"):
                raise AdopterValidationError("Search match mode must be 'all' or 'any'.")

            # Split search input into separate keywords
            terms = [word.strip() for word in search_query.split() if word.strip()]

            return AdopterManager.get_adopters(
                terms=terms,
                match_mode=match_mode,
                sort_by=sort_by,
                order=order,
            )
        except AdopterError:
            raise
        except Exception as e:
            raise AdopterError("An unexpected error occurred while loading adopters.") from e

    @staticmethod
    def fetch_adopter_details(adopter_id):
        # Fetch adopter and access their submitted adoption applications
        try:
            adopter = AdopterManager.get_adopter_by_id(adopter_id)
            if adopter is None:
                raise AdopterNotFoundError(f"Adopter with ID {adopter_id} was not found.")

            # Pre-load related applications and their associated pets
            for application in adopter.applications:
                _ = application.pet

            return adopter
        except AdopterError:
            raise
        except Exception as e:
            raise AdopterError("An error occurred while loading adopter applications.") from e