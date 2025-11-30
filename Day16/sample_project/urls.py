"""
Day 16: URL Configuration

This module shows how to configure URLs for API endpoints and documentation.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from .views import CategoryViewSet, PostViewSet, CommentViewSet


# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


# URL patterns
urlpatterns = [
    # API endpoints (from router)
    path('api/', include(router.urls)),
    
    # Authentication
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


"""
Available Endpoints:
====================

Authentication:
- POST /api/auth/token/           - Obtain auth token

Categories:
- GET /api/categories/            - List all categories
- POST /api/categories/           - Create a category (admin only)
- GET /api/categories/{id}/       - Get category details
- PUT /api/categories/{id}/       - Update category (admin only)
- DELETE /api/categories/{id}/    - Delete category (admin only)

Posts:
- GET /api/posts/                 - List all posts
- POST /api/posts/                - Create a post (authenticated)
- GET /api/posts/{id}/            - Get post details
- PUT /api/posts/{id}/            - Update post (owner only)
- DELETE /api/posts/{id}/         - Delete post (owner only)
- POST /api/posts/{id}/increment_views/  - Increment view count
- GET /api/posts/my_posts/        - Get current user's posts

Comments:
- GET /api/comments/              - List all comments
- POST /api/comments/             - Create a comment (authenticated)
- GET /api/comments/{id}/         - Get comment details
- PUT /api/comments/{id}/         - Update comment (author only)
- DELETE /api/comments/{id}/      - Delete comment (author or post author)

Documentation:
- GET /api/schema/                - OpenAPI schema (JSON)
- GET /api/docs/                  - Swagger UI
- GET /api/redoc/                 - ReDoc documentation

Query Parameters:
=================

Posts:
- ?status=published               - Filter by status
- ?category=1                     - Filter by category ID
- ?search=django                  - Search in title/content
- ?ordering=-created_at           - Order by field
- ?page=2                         - Pagination
- ?page_size=20                   - Items per page

Comments:
- ?post=1                         - Filter by post ID
- ?is_approved=true               - Filter by approval status
"""
