# Author: Elias Arriaga
# Date: 11/18/2026
# File: adopter_controller.py
# Description: Controller handling application logic between adopter routes and the adopter manager.

from app.adopter.adopter_manager import AdopterManager
from app.adopter.adopter_exceptions import AdopterError

class AdopterController:
    @staticmethod
    def fetch_all_adopters():
        # Request adopter records from the manager and handle application logic
        try:
            adopters = AdopterManager.get_all_adopters()
            if adopters is None:
                return []
            return adopters
        except AdopterError:
            raise
        except Exception as e:
            raise AdopterError("An error occurred while processing adopter data.") from e