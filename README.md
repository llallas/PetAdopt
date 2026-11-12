# Pet Adoption System — Phase 2

## Team Member Contributions
- Elias: Set up project structure, `database.py`, `extensions.py`, and centralized error handling, Implemented exceptions, HTML templates and CSS styling.

- Carolyn: Implemented `shelter` and `breed` models, managers, routes, and custom exceptions, `adopter` model, manager, routes, custom. 




## Instructions for Installing Dependencies

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Activate the virtual environment. On macOS run:

   ```bash
   source .venv/bin/activate
   ```

   On Windows PowerShell, run:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the required packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Make sure `pet_adoption.sqlite` is in the project folder beside `main.py`, then start the app:

   ```bash
   python main.py
   ```

5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. Use the navigation links to view Shelters, Breeds, and Adopters.