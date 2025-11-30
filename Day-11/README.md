# Day 11: Django Part 1 - Setup & Basics

## 📚 Overview

Welcome to Day 11! Today we dive into Django, one of the most popular and powerful Python web frameworks. Django follows the "batteries-included" philosophy, providing everything you need to build web applications quickly and efficiently.

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:
- Install Django and create a new project
- Understand Django's project structure
- Create and configure Django apps
- Set up URL routing
- Create function-based views
- Use Django templates for HTML rendering
- Build a complete "Hello World" Django application

---

## 📖 Lesson Content

### 1. What is Django?

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development so you can focus on writing your app.

**Key Features:**
- **MTV Architecture**: Model-Template-View (similar to MVC)
- **ORM**: Built-in database abstraction layer
- **Admin Interface**: Automatic admin panel
- **Security**: Protection against common vulnerabilities
- **Scalability**: Powers sites like Instagram, Pinterest, and Disqus

### 2. Django Installation

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Django
pip install django

# Verify installation
python -m django --version
```

### 3. Creating a Django Project

```bash
# Create a new Django project
django-admin startproject myproject

# Navigate into the project
cd myproject

# Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the Django welcome page!

### 4. Django Project Structure

```
myproject/
├── manage.py           # Command-line utility for admin tasks
└── myproject/          # Project package
    ├── __init__.py     # Python package marker
    ├── settings.py     # Project settings/configuration
    ├── urls.py         # URL declarations (routing)
    ├── asgi.py         # ASGI entry point (async server)
    └── wsgi.py         # WSGI entry point (production server)
```

**Key Files Explained:**
- **manage.py**: Your project's command-line interface
- **settings.py**: Database config, installed apps, middleware, templates config
- **urls.py**: URL patterns that map URLs to views

### 5. Creating a Django App

Django projects consist of multiple "apps" - self-contained modules for specific functionality.

```bash
# Create a new app
python manage.py startapp myapp
```

**App Structure:**
```
myapp/
├── __init__.py     # Python package marker
├── admin.py        # Admin interface configuration
├── apps.py         # App configuration
├── migrations/     # Database migration files
├── models.py       # Database models
├── tests.py        # Unit tests
└── views.py        # View functions/classes
```

**Register the app in settings.py:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add your app here
]
```

### 6. URL Routing

Django uses URL patterns to route requests to the appropriate view.

**Project-level urls.py:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include app URLs
]
```

**App-level urls.py (create this file in your app):**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

**URL Pattern Examples:**
- `path('', views.home)` - Matches root URL
- `path('about/', views.about)` - Matches `/about/`
- `path('user/<int:id>/', views.user)` - Matches `/user/123/`
- `path('hello/<str:name>/', views.hello)` - Matches `/hello/john/`

### 7. Function-Based Views

Views handle the logic of your application and return responses.

```python
# views.py
from django.shortcuts import render
from django.http import HttpResponse

# Simple HTTP Response
def home(request):
    return HttpResponse("Welcome to my Django app!")

# Using Templates
def about(request):
    return render(request, 'about.html')

# View with URL parameters
def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)

# View with query parameters
def search(request):
    query = request.GET.get('q', '')
    return HttpResponse(f"Searching for: {query}")
```

### 8. Django Templates

Templates are HTML files with Django template language (DTL).

**Create templates folder:**
```
myapp/
└── templates/
    └── myapp/
        ├── base.html
        ├── home.html
        └── hello.html
```

**base.html (Template inheritance):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 My Django App</p>
    </footer>
</body>
</html>
```

**home.html:**
```html
{% extends 'myapp/base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome to Django!</h1>
    <p>This is the home page.</p>
{% endblock %}
```

**Template Tags and Filters:**
```html
<!-- Variables -->
<p>Hello, {{ name }}!</p>

<!-- Filters -->
<p>{{ name|upper }}</p>
<p>{{ text|truncatewords:30 }}</p>

<!-- If statement -->
{% if user.is_authenticated %}
    <p>Welcome back, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}

<!-- For loop -->
{% for item in items %}
    <li>{{ item }}</li>
{% empty %}
    <li>No items found.</li>
{% endfor %}

<!-- URL tag -->
<a href="{% url 'hello' name='John' %}">Say Hello to John</a>
```

---

## 🛠️ Quick Project: Hello World Django App

Follow these steps to build your first Django app:

### Step 1: Set up the project

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django
pip install django

# Create project
django-admin startproject hello_world_project
cd hello_world_project

# Create app
python manage.py startapp greetings
```

### Step 2: Register the app

Edit `hello_world_project/settings.py`:
```python
INSTALLED_APPS = [
    # ... existing apps ...
    'greetings',
]
```

### Step 3: Create views

Edit `greetings/views.py`:
```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'greetings/home.html')

def hello(request, name):
    context = {'name': name}
    return render(request, 'greetings/hello.html', context)
```

### Step 4: Create URL routes

Create `greetings/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/<str:name>/', views.hello, name='hello'),
]
```

Update `hello_world_project/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greetings.urls')),
]
```

### Step 5: Create templates

Create the directory structure:
```
greetings/
└── templates/
    └── greetings/
        ├── base.html
        ├── home.html
        └── hello.html
```

### Step 6: Run the server

```bash
python manage.py runserver
```

Visit:
- `http://127.0.0.1:8000/` - Home page
- `http://127.0.0.1:8000/hello/YourName/` - Personalized greeting

---

## 📁 Project Files

The complete Hello World project is included in this folder:

```
Day-11/
├── README.md                 # This file
├── assessment.md            # Daily test
└── hello_world_project/     # Complete Django project
    ├── manage.py
    ├── hello_world_project/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    └── greetings/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── views.py
        ├── urls.py
        └── templates/
            └── greetings/
                ├── base.html
                ├── home.html
                └── hello.html
```

---

## 🎓 Key Takeaways

1. **Django Structure**: Projects contain apps; apps are reusable modules
2. **MTV Pattern**: Model (data), Template (presentation), View (logic)
3. **URL Routing**: Maps URLs to views using urlpatterns
4. **Function-Based Views**: Python functions that handle requests
5. **Templates**: HTML files with Django template language for dynamic content

---

## 📚 Additional Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

---

## ⏭️ What's Next?

In **Day 12**, we'll learn about:
- Django Models and ORM
- Database migrations
- Django Admin interface
- Building a Blog with posts

---

**Remember:** Practice is key! Modify the Hello World app by:
- Adding more views
- Creating additional URL patterns
- Experimenting with template tags and filters
