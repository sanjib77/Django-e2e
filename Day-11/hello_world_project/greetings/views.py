"""
Views for the greetings app.

This module contains function-based views that demonstrate:
- Simple views returning rendered templates
- Views with URL parameters
- Passing context data to templates
"""
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """
    Home page view.
    
    Renders the home page template with a welcome message.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse with rendered home.html template
    """
    return render(request, 'greetings/home.html')


def hello(request, name):
    """
    Personalized greeting view.
    
    Renders a greeting page with a personalized message using
    the name from the URL parameter.
    
    Args:
        request: HttpRequest object
        name: String from URL parameter
        
    Returns:
        HttpResponse with rendered hello.html template and context
    """
    context = {
        'name': name,
    }
    return render(request, 'greetings/hello.html', context)


def about(request):
    """
    About page view (example for assessment).
    
    A simple view that renders an about page template.
    
    Args:
        request: HttpRequest object
        
    Returns:
        HttpResponse with rendered about.html template
    """
    return render(request, 'greetings/about.html')
