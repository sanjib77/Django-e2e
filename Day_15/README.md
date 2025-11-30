# Day 15: Django REST Framework Basics

## 📚 Overview

Welcome to Day 15 of the intensive bootcamp! Today we dive into APIs and the Django REST Framework (DRF). This is where your Django skills transform into building modern, scalable web services.

## 🎯 Learning Objectives

By the end of this day, you will be able to:

1. Understand what APIs are and why they matter
2. Install and configure Django REST Framework
3. Create serializers to convert data between Python objects and JSON
4. Build API views and viewsets
5. Test your APIs using built-in tools

## 📋 Topics Covered

| Topic | Duration | Description |
|-------|----------|-------------|
| Why APIs? | 15 min | Understanding REST APIs and their importance |
| Installing DRF | 10 min | Setup and configuration |
| Serializers | 20 min | Data serialization concepts |
| API Views & ViewSets | 25 min | Building API endpoints |
| Practice | 20 min | Hands-on coding |

## 📁 Files in This Folder

- `01_why_apis.md` - Introduction to APIs and REST concepts
- `02_installing_drf.md` - Installation and setup guide
- `03_serializers.md` - Understanding serializers
- `04_views_and_viewsets.md` - Building API views
- `code_examples/` - Working code examples
- `daily_test.md` - Day 15 assessment (10 questions)

## 🚀 Quick Start

```bash
# Create a new Django project (if starting fresh)
django-admin startproject api_project
cd api_project

# Install DRF
pip install djangorestframework

# Add to INSTALLED_APPS in settings.py
# 'rest_framework',

# Create your first API app
python manage.py startapp api
```

## 📝 Key Takeaways

1. **APIs** = Application Programming Interfaces - they let different software talk to each other
2. **REST** = Representational State Transfer - a standard way to structure APIs
3. **DRF** = Django REST Framework - makes building APIs in Django super easy
4. **Serializers** = Convert Django models to/from JSON
5. **ViewSets** = Group related views together for cleaner code

## ⏰ Estimated Time: 2-3 hours

Let's build your first API! 🎉
