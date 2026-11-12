# Author: Elias & Carolyn
# Date: 11/11/26
# File: vaccination_model.py
# Description: Define the Vaccination model for the database

from extensions import db


class Vaccination(db.Model):
    __tablename__ = "vaccination"

    vaccination_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer, db.ForeignKey("pet.pet_id"), nullable=False)
    vaccine_name = db.Column(db.Text, nullable=False)
    vaccination_date = db.Column(db.Text, nullable=False)
    expiration_date = db.Column(db.Text)