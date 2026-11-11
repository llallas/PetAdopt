# Author: Elias & Carolyn
# Date: 11/11/2026
# File: breed_model.py
# Description: Define the Breed model for the database

from extensions import db

class Breed(db.Model):
    __tablename__ = "breed"

    breed_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    breed_name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)