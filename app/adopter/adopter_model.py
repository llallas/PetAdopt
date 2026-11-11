# Author: Elias & Carolyn
# Date: 11/11/2026
# File: adopter_model.py
# Description: Define the Adopter model for the database

from extensions import db

class Adopter(db.Model):
    __tablename__ = "adopter"

    adopter_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)