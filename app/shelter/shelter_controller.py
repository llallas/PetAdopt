# Author: Elias Arriaga
# Date: 11/18/2026
# File: shelter_controller.py
# Description: Controller handling application logic between shelter routes and the shelter manager.

from app.shelter.shelter_manager import ShelterManager
from app.shelter.shelter_exceptions import ShelterError


class ShelterController:
    @staticmethod
    def fetch_all_shelters(search=""):
        # Pass the search text to the manager.
        try:
            shelters = ShelterManager.get_all_shelters(search)
            if shelters is None:
                return []
            return shelters
        except ShelterError:
            raise
        except Exception as e:
            raise ShelterError(
                "An error occurred while processing shelter data."
            ) from e

    @staticmethod
    def fetch_shelter(shelter_id):
        # Request one shelter and its pets from the manager.
        try:
            return ShelterManager.get_shelter(shelter_id)
        except ShelterError:
            raise
        except Exception as e:
            raise ShelterError(
                "An error occurred while processing the shelter details."
            ) from e