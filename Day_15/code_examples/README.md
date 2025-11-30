# Code Examples for Day 15

This folder contains working code examples for Django REST Framework basics.

## Files

1. `models.py` - Sample Django models
2. `serializers.py` - DRF serializers
3. `views.py` - API views (function-based, class-based, and ViewSets)
4. `urls.py` - URL routing configuration

## Quick Start

1. Copy these files to your Django app
2. Run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Run server: `python manage.py runserver`
4. Visit `http://localhost:8000/api/` to test

## Project Setup Commands

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django djangorestframework

# Create project
django-admin startproject bookstore_api
cd bookstore_api

# Create app
python manage.py startapp books

# Copy the example files to the books app
# Then add 'rest_framework' and 'books' to INSTALLED_APPS

# Run migrations
python manage.py makemigrations books
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/books/` | GET | List all books |
| `/api/books/` | POST | Create a book |
| `/api/books/<id>/` | GET | Get single book |
| `/api/books/<id>/` | PUT | Update book |
| `/api/books/<id>/` | DELETE | Delete book |
| `/api/books/in_stock/` | GET | List books in stock |
