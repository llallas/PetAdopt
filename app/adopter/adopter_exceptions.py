# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_exceptions.py
# Description: Define custom exceptions for adopter-related errors

#Base exception for adopter-related errors.
class AdopterError(Exception):
    pass

#Raised when a database operation fails for adopters.
class AdopterDatabaseError(AdopterError):
    pass