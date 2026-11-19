# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_manager.py
# Description: Manage adopter-related operations and interactions with the database

from sqlalchemy import and_, or_
from sqlalchemy.exc import SQLAlchemyError
from app.adopter.adopter_model import Adopter
from app.adopter.adopter_exceptions import AdopterDatabaseError


class AdopterManager:
    # Map allowed sort query values to Adopter name columns
    SORT_FIELDS = {
        "last_name": Adopter.last_name,
        "first_name": Adopter.first_name,
    }

    @staticmethod
    def get_adopters(terms=None, match_mode="all", sort_by="last_name", order="asc"):
        # Query adopters with optional keyword search and sorting by first or last name
        try:
            query = Adopter.query

            # Apply multi-term pattern matching if search terms were entered
            if terms:
                term_conditions = []
                for term in terms:
                    pattern = f"%{term}%"
                    term_conditions.append(
                        or_(
                            Adopter.first_name.like(pattern),
                            Adopter.last_name.like(pattern),
                            Adopter.email.like(pattern),
                        )
                    )

                if match_mode == "any":
                    query = query.filter(or_(*term_conditions))
                else:
                    query = query.filter(and_(*term_conditions))

            # Sort adopters by first_name or last_name (ascending or descending)
            sort_column = AdopterManager.SORT_FIELDS.get(sort_by, Adopter.last_name)
            if order == "desc":
                query = query.order_by(sort_column.desc())
            else:
                query = query.order_by(sort_column.asc())

            return query.all()
        except SQLAlchemyError as e:
            raise AdopterDatabaseError("Failed to retrieve adopters from the database.") from e

    @staticmethod
    def get_adopter_by_id(adopter_id):
        # Retrieve a single adopter record by primary key
        try:
            return Adopter.query.get(adopter_id)
        except SQLAlchemyError as e:
            raise AdopterDatabaseError("Failed to retrieve adopter details from the database.") from e