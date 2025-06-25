# Coderr-Backend
Backend Applicaton for Coderr.

Website:
    - folgt

GitHub:
    `git clone https://github.com/dampolo/coderrbackend.git`

# Description
The Coderr backend is a robust REST API built with Django and Django REST Framework (DRF). It supports functionalities such as user authentication, password reset, profile management, and review systems for business users.

## Technologies
- Django: 5.2
- Django REST Framework: For API development  
- SQLite: Standard database (can be configured)  

## Installation

### Requirements
Make sure you have Python 3.13 or higher and pip installed.

1. Clone the repository:  
   `git clone https://github.com/dampolo/coderrbackend.git`

2. Create and activate a virtual environment with the following commands:  
   `"env/Scripts/activate" or env/Scripts/activate`  
   `source env/bin/activate   # On Windows: env/Scripts/activate`

   You should see on the left, next to path (env)

3. Install the dependencies:  
   `pip install -r requirements.txt`

4. Configure the database:  
   Run the migrations to initialize the database:  
   `python manage.py migrate`
   `python manage.py makemigrations`

5. Start the development server:  
   `python manage.py runserver`

## Troubleshooting
If you encounter issues, check the following:

- Ensure that the database is correctly configured and migrations have been run.
- Verify the `requirements.txt` for the correct dependency versions.

## Contributors
Damian Poloczek

