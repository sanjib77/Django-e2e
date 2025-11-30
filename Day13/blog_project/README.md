# Blog Project with User Authentication

This is a practical Django blog project demonstrating:
- Django Forms
- Form Validation
- User Authentication (Login, Logout, Register)
- Protected Views with @login_required

## Setup Instructions

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Django
```bash
pip install django
```

### 3. Create Django Project
```bash
django-admin startproject blog_project .
cd blog_project
python manage.py startapp blog
```

### 4. Configure Settings

Add to `blog_project/settings.py`:
```python
INSTALLED_APPS = [
    # ... default apps
    'blog',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        # ... rest of settings
    },
]

# Authentication settings
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
```

### 5. Create Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/accounts/login/
- Register: http://127.0.0.1:8000/register/

## Project Files

- `blog/models.py` - Post model
- `blog/forms.py` - User registration and post forms
- `blog/views.py` - View functions with authentication
- `blog/urls.py` - URL routing
- `templates/` - HTML templates

## Features

1. **User Registration** - Create new accounts
2. **User Login/Logout** - Session-based authentication
3. **Create Posts** - Only authenticated users
4. **Edit/Delete Posts** - Only by post author
5. **User Profile** - View own posts
