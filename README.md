E-commerce Website

A fully functional E-commerce website built with Django. This project includes product management, user authentication, and REST API endpoints for products and categories.

Features

User registration, login, and logout

Product CRUD operations

Category CRUD operations

REST API endpoints for products and categories

Admin dashboard for site management

SQLite database (can be changed to PostgreSQL or MySQL)

Tech Stack

Backend: Python, Django, Django REST Framework

Database: SQLite

API Testing: Thunder Client / Postman

Installation

Clone the repository:

git clone <your-repo-link>
cd E-commerce-Website


Create a virtual environment:

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser for admin access:

python manage.py createsuperuser


Run the development server:

python manage.py runserver

Usage

Access the website at: http://127.0.0.1:8000/

Access the admin panel at: http://127.0.0.1:8000/admin/

Use Thunder Client or Postman to test the API endpoints:

/api/products/

/api/categories/

Contributing

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Make your changes

Commit (git commit -m "Add your message")

Push (git push origin feature/your-feature)

Open a Pull Request

License

This project is licensed under the MIT License.
