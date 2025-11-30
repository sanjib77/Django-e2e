# Local Deployment Guide

## 🚀 Deploying the Blog Application Locally

This guide walks you through deploying the Day 14 Blog application on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)

## Step-by-Step Deployment

### 1. Clone the Repository (if not already done)

```bash
git clone <repository-url>
cd Django-e2e/Day14
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to isolate project dependencies.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Navigate to the Project Directory

```bash
cd blog_project
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

This creates the SQLite database and sets up all necessary tables.

### 6. Create a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your web browser and navigate to:

- **Blog Homepage:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/

## Testing the Application

### Test User Registration

1. Go to http://127.0.0.1:8000/accounts/register/
2. Create a new account
3. You should be logged in automatically

### Test CRUD Operations

1. **Create:** Click "New Post" to create a blog post
2. **Read:** View posts on the homepage and click to see details
3. **Update:** Click "Edit" on your own posts
4. **Delete:** Click "Delete" on your own posts

### Test Authentication

1. **Logout:** Click the logout button
2. **Login:** Go to login page and sign in
3. **Protected Routes:** Try creating a post without logging in

## Common Issues & Solutions

### Issue: "No module named 'django'"
**Solution:** Make sure you activated the virtual environment and installed requirements.

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: "TemplateDoesNotExist"
**Solution:** Make sure you're running from the correct directory (blog_project/).

### Issue: Database errors
**Solution:** Delete db.sqlite3 and run migrations again.

```bash
rm db.sqlite3
python manage.py migrate
```

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the development server.

## Production Deployment Notes

For production deployment, you would need to:

1. Set `DEBUG = False` in settings.py
2. Configure a production-ready database (PostgreSQL)
3. Set up a web server (Nginx/Apache)
4. Use a WSGI server (Gunicorn/uWSGI)
5. Configure static files serving
6. Set up HTTPS with SSL certificate

This is covered in Week 6 (Day 39: Cloud Deployment Basics).

## Quick Reference Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Run on different port
python manage.py runserver 8080

# Make migrations after model changes
python manage.py makemigrations

# Open Django shell
python manage.py shell
```

---

**Happy Coding! 🎉**
