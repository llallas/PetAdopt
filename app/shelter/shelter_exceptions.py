# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_exceptions.py
# Description: Define custom exceptions for shelter-related errors

# Base exception for shelter-related errors.
class ShelterError(Exception):
    pass

#Raised when a database operation fails for shelters.
class ShelterDatabaseError(ShelterError):
    pass