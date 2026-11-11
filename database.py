# Author: Elias & Carolyn
# Date: 11/11/2026
# File: database.py
# Description: Initialize the database connection and configuration

import os
from pathlib import Path

from extensions import db


def init_db(app):
    base_dir = Path(__file__).resolve().parent
    db_path = base_dir / "pet_adoption.sqlite"

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)