# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_exceptions.py
# Description: Define custom exceptions for breed-related errors

# Base exception for breed-related errors.
class BreedError(Exception):
    pass

    # Raised when a database operation fails for breeds.
class BreedDatabaseError(BreedError):
    pass