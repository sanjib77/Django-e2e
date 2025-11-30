"""
URL configuration for the greetings app.

This module defines URL patterns that map URLs to views.
It demonstrates:
- Basic URL patterns
- URL patterns with string parameters
- Named URL patterns (for use with {% url %} template tag)
"""
from django.urls import path
from . import views

urlpatterns = [
    # Home page - matches root URL
    path('', views.home, name='home'),
    
    # Personalized greeting - matches /hello/<name>/
    # <str:name> captures a string parameter from the URL
    path('hello/<str:name>/', views.hello, name='hello'),
]
