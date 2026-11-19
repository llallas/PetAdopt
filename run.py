# Author: Elias & Carolyn
# Date: 11/18/2026
# File: run.py
# Entry point for starting the Flask development server.

from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the application in debug mode for development
    app.run(debug=True)