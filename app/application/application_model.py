# Author: Elias & Carolyn
# Date: 11/11/26
# File: application_model.py
# Description: Define the Application model for the database

from extensions import db


class Application(db.Model):
    __tablename__ = "application"

    application_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adopter_id = db.Column(db.Integer, db.ForeignKey("adopter.adopter_id"), nullable=False)
    pet_id = db.Column(db.Integer, db.ForeignKey("pet.pet_id"), nullable=False)
    application_date = db.Column(db.Text, nullable=False)
    application_status = db.Column(db.Text, nullable=False)
    decision_date = db.Column(db.Text)