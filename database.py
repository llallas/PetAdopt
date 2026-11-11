# Author: Elias & Carolyn
# Date: 11/11/2026
# File: database.py
# Description: Initialize the database connection and configuration

import os
from extensions import db

def init_db(app):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "pet_adoption.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)