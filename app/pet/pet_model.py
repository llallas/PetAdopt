# Author: Elias & Carolyn
# Date: 11/11/26
# File: pet_model.py
# Description: Define the Pet model for the database

from extensions import db


class Pet(db.Model):
    __tablename__ = "pet"

    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shelter_id = db.Column(db.Integer, db.ForeignKey("shelter.shelter_id"), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey("breed.breed_id"), nullable=False)
    name = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.Text)
    color = db.Column(db.Text)
    sex = db.Column(db.Text, nullable=False)
    spay_neuter_status = db.Column(db.Text, nullable=False)
    intake_date = db.Column(db.Text, nullable=False)
    adoption_status = db.Column(db.Text, nullable=False)