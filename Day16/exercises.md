# Day 16: Quick Practice Exercises - Secure Your API

## 🎯 Objective

Practice implementing authentication, permissions, filtering, and pagination in a Django REST Framework API.

---

## Exercise 1: Set Up Token Authentication

### Task

Add token authentication to an existing DRF project.

### Requirements

1. Install and configure `rest_framework.authtoken`
2. Create a token endpoint at `/api/auth/token/`
3. Test obtaining a token with valid credentials

### Starter Code

```python
# settings.py - Add the necessary configuration

INSTALLED_APPS = [
    # Add the auth token app here
]

REST_FRAMEWORK = {
    # Add authentication classes here
}
```

### Expected Result

- POST to `/api/auth/token/` with username/password returns a token
- Token can be used in subsequent requests

---

## Exercise 2: Implement Custom Permission

### Task

Create a custom permission that only allows the creator of an object to modify or delete it.

### Requirements

1. Create a new file `permissions.py`
2. Implement `IsCreatorOrReadOnly` permission class
3. Apply it to a ViewSet

### Starter Code

```python
# permissions.py

from rest_framework import permissions

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only the creator can edit/delete.
    Anyone can read.
    """
    
    def has_object_permission(self, request, view, obj):
        # TODO: Implement this method
        # Hint: Check if request.method is in SAFE_METHODS
        # Hint: Compare obj.creator with request.user
        pass
```

### Test Your Implementation

1. Create an object as User A
2. Try to update it as User B (should fail with 403)
3. Try to update it as User A (should succeed)
4. Try to read it as User B (should succeed)

---

## Exercise 3: Add Filtering to Your API

### Task

Add comprehensive filtering to a blog post API.

### Requirements

1. Install `django-filter`
2. Enable filtering by: `author`, `status`, `category`
3. Enable search in: `title`, `content`
4. Enable ordering by: `created_at`, `updated_at`, `title`

### Starter Code

```python
# views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    # TODO: Add filter_backends
    # TODO: Add filterset_fields
    # TODO: Add search_fields
    # TODO: Add ordering_fields
```

### Test Your Implementation

Try these URLs:
- `/api/posts/?author=1`
- `/api/posts/?status=published`
- `/api/posts/?search=django`
- `/api/posts/?ordering=-created_at`
- `/api/posts/?author=1&status=published&ordering=title`

---

## Exercise 4: Implement Custom Pagination

### Task

Create a custom pagination class with configurable page sizes.

### Requirements

1. Create `pagination.py`
2. Implement `StandardResultsPagination` class
3. Allow clients to request custom page sizes (max 100)
4. Set default page size to 20

### Starter Code

```python
# pagination.py

from rest_framework.pagination import PageNumberPagination

class StandardResultsPagination(PageNumberPagination):
    # TODO: Set page_size
    # TODO: Set page_size_query_param
    # TODO: Set max_page_size
    pass
```

### Test Your Implementation

- `/api/posts/` - Should return 20 items
- `/api/posts/?page_size=50` - Should return 50 items
- `/api/posts/?page_size=200` - Should cap at 100 items
- `/api/posts/?page=2` - Should return second page

---

## Exercise 5: Complete API Security Setup

### Task

Combine all concepts to fully secure an API endpoint.

### Requirements

Create a `ProductViewSet` with:

1. **Authentication**: Token authentication required
2. **Permissions**: 
   - List/Retrieve: Anyone (even unauthenticated)
   - Create: Authenticated users only
   - Update/Delete: Only the creator
3. **Filtering**: By `category`, `price_range`, `in_stock`
4. **Search**: In `name` and `description`
5. **Ordering**: By `price`, `created_at`, `name`
6. **Pagination**: 15 items per page, max 50

### Starter Code

```python
# models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    in_stock = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```python
# serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['creator', 'created_at', 'updated_at']
```

```python
# views.py - Complete this implementation

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# TODO: Import necessary classes

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # TODO: Add authentication_classes
    # TODO: Add permission_classes
    # TODO: Add filter_backends
    # TODO: Add filterset_fields
    # TODO: Add search_fields
    # TODO: Add ordering_fields
    # TODO: Add pagination_class
    
    def perform_create(self, serializer):
        # TODO: Save with creator
        pass
    
    def get_permissions(self):
        # TODO: Return different permissions based on action
        pass
```

---

## 🏆 Bonus Challenge: API Documentation

### Task

Add Swagger documentation to your API using drf-spectacular.

### Requirements

1. Install `drf-spectacular`
2. Configure it in settings
3. Add documentation URLs
4. Add custom descriptions to at least 3 endpoints

### Expected Result

- `/api/docs/` shows Swagger UI
- `/api/redoc/` shows ReDoc documentation
- Endpoints have meaningful descriptions

---

## ✅ Completion Checklist

Before moving on, make sure you can:

- [ ] Set up token authentication
- [ ] Obtain and use tokens in requests
- [ ] Create custom permission classes
- [ ] Apply permissions to views
- [ ] Filter API results by fields
- [ ] Search across multiple fields
- [ ] Order results by different fields
- [ ] Implement pagination
- [ ] (Bonus) Generate API documentation

---

## 📝 Daily Test

After completing the exercises, take the Day 16 assessment:

**10 Questions | 15 Minutes | 70% to Pass**

Topics covered:
- Token authentication setup and usage
- Permission classes (built-in and custom)
- Filtering with django-filter
- Search and ordering
- Pagination configuration
- API documentation basics

Good luck! 🍀
