# Author: Elias Arriaga
# Date: 11/18/2026
# File: breed_controller.py
# Description: Controller handling application logic between breed routes and the breed manager.

from app.breed.breed_manager import BreedManager
from app.breed.breed_exceptions import BreedError

class BreedController:
    @staticmethod
    def fetch_all_breeds():
        # Request breed records from the manager and handle application logic
        try:
            breeds = BreedManager.get_all_breeds()
            if breeds is None:
                return []
            return breeds
        except BreedError:
            raise
        except Exception as e:
            raise BreedError("An error occurred while processing breed data.") from e