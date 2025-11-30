"""
URL Configuration for Django REST Framework Tutorial
Day 15: Django REST Framework Basics

This file shows how to configure URLs for different view types.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


# =============================================================================
# ROUTER FOR VIEWSETS
# =============================================================================

# Create a router and register our ViewSets
router = DefaultRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'categories', views.CategoryViewSet, basename='category')


# =============================================================================
# URL PATTERNS
# =============================================================================

urlpatterns = [
    # -----------------------------------------------------------------
    # Version 1: Function-based views
    # -----------------------------------------------------------------
    path('v1/books/', views.book_list_function, name='book-list-v1'),
    path('v1/books/<int:pk>/', views.book_detail_function, name='book-detail-v1'),
    
    # -----------------------------------------------------------------
    # Version 2: Class-based APIViews
    # -----------------------------------------------------------------
    path('v2/books/', views.BookListAPIView.as_view(), name='book-list-v2'),
    path('v2/books/<int:pk>/', views.BookDetailAPIView.as_view(), name='book-detail-v2'),
    
    # -----------------------------------------------------------------
    # Version 3: Generic Views
    # -----------------------------------------------------------------
    path('v3/books/', views.BookListGeneric.as_view(), name='book-list-v3'),
    path('v3/books/<int:pk>/', views.BookDetailGeneric.as_view(), name='book-detail-v3'),
    
    # -----------------------------------------------------------------
    # Version 4: ViewSets with Router (Recommended!)
    # -----------------------------------------------------------------
    # This automatically creates:
    # - GET    /v4/books/           -> list
    # - POST   /v4/books/           -> create
    # - GET    /v4/books/{pk}/      -> retrieve
    # - PUT    /v4/books/{pk}/      -> update
    # - PATCH  /v4/books/{pk}/      -> partial_update
    # - DELETE /v4/books/{pk}/      -> destroy
    # - GET    /v4/books/in_stock/  -> in_stock (custom action)
    # - POST   /v4/books/{pk}/toggle_stock/ -> toggle_stock (custom action)
    path('v4/', include(router.urls)),
]


# =============================================================================
# MAIN PROJECT URLs (for reference)
# =============================================================================

"""
In your main project's urls.py (e.g., bookstore_api/urls.py), add:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),  # Your API app
    
    # DRF's browsable API authentication (optional but recommended)
    path('api-auth/', include('rest_framework.urls')),
]

This will make your API available at:
- http://localhost:8000/api/v1/books/
- http://localhost:8000/api/v2/books/
- http://localhost:8000/api/v3/books/
- http://localhost:8000/api/v4/books/
"""
