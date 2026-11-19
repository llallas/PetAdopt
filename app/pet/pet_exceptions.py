# Author: Elias Arriaga
# Date: 11/18/2026
# File: pet_exceptions.py
# Description: This module defines custom exceptions for handling errors related to pet operations in the application.

#Base exception for pet-related errors.
class PetError(Exception):
    pass

#Raised when filter, sort, or limit query parameters are invalid.
class PetValidationError(PetError):
    pass

#Raised when a requested pet ID does not exist.
class PetNotFoundError(PetError):
    pass

# Raised when a database query fails for pets.
class PetDatabaseError(PetError):
    pass