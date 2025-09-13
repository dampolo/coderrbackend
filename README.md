# Coderr Backend

A Django backend for a JavaScript-based freelancer platform. This repository provides the server-side application, handling authentication, project management, and other API endpoints to support a dynamic freelancer marketplace.

---

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies](#technologies)
- [Database](#Database)
- [Installation](#installation)
---

## About

**Coderr Backend** is built using Django and is designed to serve as the backend of a freelancer developer platform. It manages user authentication, project-related operations, and provides API endpoints that allow seamless integration with a JavaScript-based frontend. This project is structured to be modular, secure, and extendable.

---

## Features

- **User Authentication:** Secure registration, login, and profile management.
- **Project Management:** API endpoints for offering, ordering and reviewing software services.
- **Modular Architecture:** Organized into separate Django apps for the accordingly feature: coderr_backend as coderr, auth_app, offers_app, orders_app, reviews_app, base_info_app
- **Media Management:** Handles file uploads (e.g., profile images, project documents) stored in `/media/images`.
- **RESTful API Design:** Easy integration with modern JavaScript front-end frameworks.

---

## Technologies

- **Python 3** – The programming language used.
- **Django** – The high-level Python web framework powering the backend.
- **Django REST Framework:** For building RESTful APIs.
- **PostgreSQL:** on the production: https://coderr.damianpoloczek.com/.
- **SQLite:** The default development database.

Additional dependencies can be found in the [requirements.txt](requirements.txt) file.

---

## Database
If you want to use SQLite as your database, go to:
coderr_backend/coderr/settings.py and comment out lines 112–117 (the current database configuration).

On the production we are using PostgreSQL Verison 17.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone git@github.com:dampolo/coderrbackend.git
   ```

2. Create and activate a virtual environment with the following commands:
   
   A. Creat virtual environment
   ```bash
   python3 -m venv env
   ```

   B. Activate virtual environment

   On Windows
   ```bash
   "env/Scripts/activate"
   ```

   or if it does not work, try like follow
   ```bash
   env/Scripts/activate
   ```
   
   On Mac/Linux
   ```bash     
   source env/bin/activate
   ```
   
   Finally: You should see on the left, next to path (env)

   ```bash
   (env) you/pfad/to/project>
   ```


3. Install the dependencies:

   ```bash
   pip install -r requirements.txt

4. Configure the database:  
   Run the migrations to initialize the database:
   
   ```bash
   python manage.py makemigrations
   ```
   and
   ```bash
   python manage.py migrate

5. Start the development server:  
   
   ```bash
   python manage.py runserver
   
The backend should now be running at:
http://127.0.0.1:8000/