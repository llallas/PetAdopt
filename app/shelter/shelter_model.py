# Author: Elias & Carolyn
# Date: 11/11/2026
# File: shelter_model.py
# Description: Define the Shelter model for the pet adoption application

from extensions import db

class Shelter(db.Model):
    __tablename__ = "shelter"

    shelter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    street_address = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    zip_code = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)