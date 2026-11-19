# Pet Adoption System — Phase 2

## Team Member Contributions
- Elias: Set up the Flask application and centralized exception handling. Added pet filtering, sorting, result limits, pet details, and adopter searching, sorting, and application details.
- Carolyn: Created the database and implemented the original shelter, breed, and adopter database features. Added shelter keyword searching and shelter detail pages showing related pets. Finalized Blueprint and template organization, connected breed details through the controller, added validation error handling, and tested the updated pages.
- Both: Reviewed the project and checked that the features worked.

## Phase 3 Features

- Filter pets by breed, sex and spay/neuter status.
- Sort pets by name, intake date, or birth date in ascending or descending order.
- Limit the number of pets displayed.
- Search shelter names using multiple keywords.
- Search adopters by name or email using all keywords (AND) or any keyword (OR).
- Sort adopters by first or last name in ascending or descending order.
- View shelter details and related pets.
- View pet details with related shelter, breed, vaccination and application records.
- View adopter details and related applications.
- View breed details.
- Display error pages for invalid inputs, missing records and database errors.

## Installation and Running Instructions

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
   
5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser. Use the navigation links to view Shelters, Breeds, Pets and Adopters.