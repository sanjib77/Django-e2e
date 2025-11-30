# Day 16 Sample Project

This folder contains sample code demonstrating DRF Advanced concepts.

## Files

- `settings_snippet.py` - Django settings configuration
- `models.py` - Sample models
- `serializers.py` - DRF serializers
- `permissions.py` - Custom permission classes
- `views.py` - ViewSets with auth, permissions, filtering
- `pagination.py` - Custom pagination class
- `urls.py` - URL configuration
- `filters.py` - Custom filter classes

## How to Use

These files are meant to be integrated into your existing Django project. Copy the relevant sections into your project files.

## Quick Setup

1. Install required packages:
```bash
pip install djangorestframework django-filter drf-spectacular
```

2. Add to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_spectacular',
]
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Start the server:
```bash
python manage.py runserver
```

6. Test the API at http://localhost:8000/api/
