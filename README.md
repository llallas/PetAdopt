# Pet Adoption System

A Flask web application built with MVC architecture, Blueprints, and Flask-SQLAlchemy to display records from the Pet Adoption SQLite database.

## Project Structure

```text
pet_adoption_app/
├── pet_adoption.db
├── database.py
├── extensions.py
├── run.py
└── app/
    ├── __init__.py
    ├── shelter/
    ├── breed/
    ├── adopter/
    ├── static/
    │   └── style.css
    └── templates/
        ├── base.html
        ├── index.html
        ├── shelters.html
        ├── breeds.html
        ├── adopters.html
        └── error.html