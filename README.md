# Pet Adoption System — Phase 2

## Team Member Contributions
- Elias: Set up project structure, `database.py`, `extensions.py`, and centralized error handling, Implemented exceptions, HTML templates and CSS styling.

- Carolyn: Implemented `shelter` and `breed` models, managers, routes, and custom exceptions, `adopter` model, manager, routes, custom. 




## Instructions for Installing Dependencies

1. Open a terminal in the project folder and create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

2. Activate it on macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Make sure `pet_adoption.sqlite` is beside `main.py`, then start the app:

   ```bash
   python main.py
   ```
   
5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. Use the navigation links to view Shelters, Breeds, and Adopters.