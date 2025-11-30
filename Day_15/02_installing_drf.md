# Installing Django REST Framework

## 🛠️ Prerequisites

Before installing DRF, make sure you have:
- Python 3.8+ installed
- Django 3.2+ installed
- A Django project ready

## 📥 Installation

### Step 1: Install DRF

```bash
pip install djangorestframework
```

### Step 2: Add to INSTALLED_APPS

Edit your `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'rest_framework',  # Add this line!
    
    # Your apps
    'api',  # Your API app
]
```

### Step 3: Configure DRF (Optional but Recommended)

Add DRF settings to `settings.py`:

```python
REST_FRAMEWORK = {
    # Default permission class
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # For learning - allows all access
    ],
    
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    # Date/time format
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}
```

## 🧪 Verify Installation

Run Django shell:

```bash
python manage.py shell
```

```python
>>> import rest_framework
>>> print(rest_framework.VERSION)
'3.14.0'  # or your version
```

## 📁 Project Structure

After setup, your project should look like:

```
api_project/
├── api_project/
│   ├── __init__.py
│   ├── settings.py      # DRF added here
│   ├── urls.py
│   └── wsgi.py
├── api/                  # Your API app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Database models
│   ├── serializers.py   # Create this! 
│   ├── views.py         # API views
│   └── urls.py          # Create this!
└── manage.py
```

## 🎨 DRF's Browsable API

One of DRF's best features is the **Browsable API** - a web interface to test your APIs!

Add to your main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # Add this for login/logout in browsable API
    path('api-auth/', include('rest_framework.urls')),
]
```

## 🚀 Quick Setup Script

Create a complete setup in minutes:

```bash
# Create project
django-admin startproject api_project
cd api_project

# Install DRF
pip install djangorestframework

# Create API app
python manage.py startapp api

# Create necessary files
touch api/serializers.py
touch api/urls.py

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## ✅ Installation Checklist

- [ ] Python 3.8+ installed
- [ ] Django installed
- [ ] DRF installed (`pip install djangorestframework`)
- [ ] `'rest_framework'` added to INSTALLED_APPS
- [ ] REST_FRAMEWORK settings configured (optional)
- [ ] API app created
- [ ] `serializers.py` file created in API app
- [ ] URLs configured

## 🔧 Common Issues

### Issue: ModuleNotFoundError
```python
ModuleNotFoundError: No module named 'rest_framework'
```
**Solution:** Make sure you installed DRF in your virtual environment:
```bash
pip install djangorestframework
```

### Issue: ImproperlyConfigured
```python
ImproperlyConfigured: Could not resolve URL for hyperlinked relationship
```
**Solution:** Add `'rest_framework'` to INSTALLED_APPS before your apps.

## 📝 requirements.txt

Don't forget to save your dependencies:

```bash
pip freeze > requirements.txt
```

Your `requirements.txt` should include:
```
Django>=3.2
djangorestframework>=3.14.0
```

---

**Next:** [Serializers](./03_serializers.md)
