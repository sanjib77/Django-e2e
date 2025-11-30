"""
Day 16: ViewSets with Authentication, Permissions, Filtering, and Pagination

This module demonstrates how to combine all DRF advanced features.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny
)
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter

from .models import Category, Post, Comment
from .serializers import (
    CategorySerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    CommentSerializer
)
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsCommentAuthorOrPostAuthor
from .filters import PostFilter, CommentFilter
from .pagination import StandardResultsPagination, SmallResultsPagination


@extend_schema_view(
    list=extend_schema(
        summary="List all categories",
        description="Returns a list of all blog categories.",
        tags=['Categories']
    ),
    create=extend_schema(
        summary="Create a category",
        description="Create a new category. Admin only.",
        tags=['Categories']
    ),
    retrieve=extend_schema(
        summary="Get category details",
        description="Returns details of a specific category.",
        tags=['Categories']
    ),
)
class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for blog categories.
    
    - Anyone can read categories
    - Only admin users can create/update/delete
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    
    # Filtering
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


@extend_schema_view(
    list=extend_schema(
        summary="List all posts",
        description="Returns a paginated list of all published blog posts.",
        parameters=[
            OpenApiParameter(name='status', description='Filter by status (draft, published, archived)'),
            OpenApiParameter(name='category', description='Filter by category ID'),
            OpenApiParameter(name='search', description='Search in title and content'),
            OpenApiParameter(name='ordering', description='Order by field (prefix with - for descending)'),
        ],
        tags=['Posts']
    ),
    create=extend_schema(
        summary="Create a post",
        description="Create a new blog post. Requires authentication.",
        tags=['Posts']
    ),
    retrieve=extend_schema(
        summary="Get post details",
        description="Returns full details of a specific post including comments.",
        tags=['Posts']
    ),
)
class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for blog posts with full CRUD operations.
    
    Features:
    - Token authentication
    - Owner-based permissions (only author can edit/delete)
    - Filtering by status, category, date range
    - Search in title and content
    - Ordering by multiple fields
    - Pagination (10 items per page)
    """
    
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    # Filtering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content', 'excerpt']
    ordering_fields = ['created_at', 'updated_at', 'views', 'title']
    ordering = ['-created_at']
    
    # Pagination
    pagination_class = StandardResultsPagination
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return PostListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return PostCreateUpdateSerializer
        return PostDetailSerializer
    
    def get_queryset(self):
        """Optimize queries with select_related."""
        queryset = super().get_queryset()
        queryset = queryset.select_related('author', 'category')
        
        # For detail view, prefetch comments
        if self.action == 'retrieve':
            queryset = queryset.prefetch_related('comments', 'comments__author')
        
        return queryset
    
    def perform_create(self, serializer):
        """Set the author to the current user when creating a post."""
        serializer.save(author=self.request.user)
    
    @action(detail=True, methods=['post'])
    def increment_views(self, request, pk=None):
        """Custom action to increment view count."""
        post = self.get_object()
        post.views += 1
        post.save()
        return Response({'views': post.views})
    
    @action(detail=False, methods=['get'])
    def my_posts(self, request):
        """Get posts by the current authenticated user."""
        if not request.user.is_authenticated:
            return Response(
                {'error': 'Authentication required'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        queryset = self.get_queryset().filter(author=request.user)
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = PostListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(
        summary="List comments",
        description="Returns a paginated list of comments. Filter by post ID.",
        tags=['Comments']
    ),
    create=extend_schema(
        summary="Create a comment",
        description="Add a comment to a post. Requires authentication.",
        tags=['Comments']
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for comments.
    
    Features:
    - Token authentication
    - Custom permissions (author or post author can delete)
    - Filtering by post, author
    - Smaller pagination for quick loading
    """
    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsCommentAuthorOrPostAuthor]
    
    # Filtering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CommentFilter
    search_fields = ['content']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    
    # Pagination
    pagination_class = SmallResultsPagination
    
    def get_queryset(self):
        """Optimize queries with select_related."""
        return super().get_queryset().select_related('author', 'post')
    
    def perform_create(self, serializer):
        """Set the author to the current user when creating a comment."""
        serializer.save(author=self.request.user)
