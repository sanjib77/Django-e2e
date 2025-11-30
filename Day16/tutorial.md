# Day 16: DRF Advanced - Complete Tutorial

## 🔐 1. Authentication (Token Auth)

### What is Token Authentication?

Token authentication is a simple way to authenticate users for APIs. When a user logs in, they receive a unique token that they include in all subsequent requests to prove their identity.

### Setting Up Token Authentication

#### Step 1: Install and Configure

First, add `rest_framework.authtoken` to your `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',  # Add this
    'myapp',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',  # Optional: for browsable API
    ],
}
```

#### Step 2: Run Migrations

```bash
python manage.py migrate
```

#### Step 3: Create Token Endpoint

```python
# urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # ... other urls
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
```

### Obtaining a Token

Users can obtain their token by sending a POST request:

```bash
curl -X POST http://localhost:8000/api/token/ \
    -H "Content-Type: application/json" \
    -d '{"username": "user", "password": "password123"}'
```

Response:
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Using the Token

Include the token in the Authorization header:

```bash
curl -X GET http://localhost:8000/api/posts/ \
    -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

### Creating Tokens Programmatically

```python
# views.py

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create a token for a user
user = User.objects.get(username='myuser')
token, created = Token.objects.get_or_create(user=user)
print(token.key)
```

### Custom Token View (with more user data)

```python
# views.py

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
```

---

## 🛡️ 2. Permissions

### Built-in Permission Classes

DRF provides several built-in permission classes:

| Permission Class | Description |
|-----------------|-------------|
| `AllowAny` | Allow unrestricted access |
| `IsAuthenticated` | Only authenticated users |
| `IsAdminUser` | Only admin users |
| `IsAuthenticatedOrReadOnly` | Authenticated for write, anyone for read |

### Setting Permissions Globally

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### Setting Permissions Per View

```python
# views.py

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})


class PublicView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Hello, everyone!'})
```

### Using Permissions with ViewSets

```python
# views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

### Creating Custom Permissions

```python
# permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        return obj.owner == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allow read access to everyone, but write access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
```

### Using Custom Permissions

```python
# views.py

from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
```

### Combining Multiple Permissions

```python
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
```

---

## 📄 3. Filtering and Pagination

### Installing django-filter

```bash
pip install django-filter
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ... other apps
    'django_filters',
]
```

### Basic Filtering Setup

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

### Filtering in Views

```python
# views.py

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Fields for exact filtering
    filterset_fields = ['author', 'status', 'category']
    
    # Fields for search (partial match)
    search_fields = ['title', 'content']
    
    # Fields for ordering
    ordering_fields = ['created_at', 'title', 'views']
    ordering = ['-created_at']  # Default ordering
```

### Using Filters via URL

```bash
# Filter by exact field
GET /api/posts/?status=published

# Search in title and content
GET /api/posts/?search=django

# Order by field
GET /api/posts/?ordering=-created_at

# Combine filters
GET /api/posts/?status=published&search=api&ordering=title
```

### Custom FilterSet

```python
# filters.py

import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    min_views = django_filters.NumberFilter(field_name='views', lookup_expr='gte')
    
    class Meta:
        model = Post
        fields = ['title', 'author', 'status', 'created_after', 'created_before', 'min_views']
```

```python
# views.py

from .filters import PostFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter
```

### Pagination

#### PageNumberPagination (Most Common)

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

Usage:
```bash
GET /api/posts/?page=2
```

Response:
```json
{
    "count": 100,
    "next": "http://localhost:8000/api/posts/?page=3",
    "previous": "http://localhost:8000/api/posts/?page=1",
    "results": [...]
}
```

#### LimitOffsetPagination

```python
# settings.py

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}
```

Usage:
```bash
GET /api/posts/?limit=20&offset=40
```

#### Custom Pagination Class

```python
# pagination.py

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
```

```python
# views.py

from .pagination import CustomPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
```

---

## 📚 4. API Documentation

### Installing drf-spectacular

```bash
pip install drf-spectacular
```

### Configuration

```python
# settings.py

INSTALLED_APPS = [
    # ... other apps
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'API documentation for my project',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
```

### Adding Documentation URLs

```python
# urls.py

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # Your API URLs
    path('api/', include('myapp.urls')),
    
    # Documentation URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

### Documenting Endpoints

```python
# views.py

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @extend_schema(
        summary="List all posts",
        description="Returns a paginated list of all blog posts.",
        parameters=[
            OpenApiParameter(name='status', description='Filter by status', type=str),
            OpenApiParameter(name='search', description='Search in title and content', type=str),
        ],
        responses={200: PostSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new post",
        description="Create a new blog post. Requires authentication.",
        responses={201: PostSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
```

### Adding Tags for Organization

```python
# views.py

from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(tags=['Posts']),
    create=extend_schema(tags=['Posts']),
    retrieve=extend_schema(tags=['Posts']),
    update=extend_schema(tags=['Posts']),
    partial_update=extend_schema(tags=['Posts']),
    destroy=extend_schema(tags=['Posts']),
)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

---

## 🎯 Summary

Today you learned:

1. **Token Authentication**: How to set up and use token-based auth for securing your API
2. **Permissions**: Built-in and custom permissions to control access
3. **Filtering & Pagination**: How to filter, search, order, and paginate results
4. **API Documentation**: Auto-generating beautiful API docs with Swagger/OpenAPI

These features are essential for building production-ready APIs!

---

## 📖 Additional Resources

- [DRF Authentication Documentation](https://www.django-rest-framework.org/api-guide/authentication/)
- [DRF Permissions Documentation](https://www.django-rest-framework.org/api-guide/permissions/)
- [django-filter Documentation](https://django-filter.readthedocs.io/)
- [drf-spectacular Documentation](https://drf-spectacular.readthedocs.io/)

---

Next up: **Day 17 - FastAPI Introduction** 🚀
