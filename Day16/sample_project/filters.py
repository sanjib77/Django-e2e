"""
Day 16: Custom Filter Classes

django-filter provides powerful filtering capabilities for DRF.
"""

import django_filters
from .models import Post, Comment


class PostFilter(django_filters.FilterSet):
    """
    Custom filter for Post model.
    
    Supports filtering by:
    - title (partial match)
    - author (exact)
    - category (exact)
    - status (exact)
    - date range
    - minimum views
    """
    
    # Partial match on title
    title = django_filters.CharFilter(lookup_expr='icontains')
    
    # Date range filters
    created_after = django_filters.DateFilter(
        field_name='created_at', 
        lookup_expr='gte',
        label='Created after'
    )
    created_before = django_filters.DateFilter(
        field_name='created_at', 
        lookup_expr='lte',
        label='Created before'
    )
    
    # Numeric range
    min_views = django_filters.NumberFilter(
        field_name='views', 
        lookup_expr='gte',
        label='Minimum views'
    )
    max_views = django_filters.NumberFilter(
        field_name='views', 
        lookup_expr='lte',
        label='Maximum views'
    )
    
    # Filter by author username
    author_username = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        label='Author username'
    )
    
    # Filter by category name
    category_name = django_filters.CharFilter(
        field_name='category__name',
        lookup_expr='icontains',
        label='Category name'
    )
    
    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'category',
            'status',
            'created_after',
            'created_before',
            'min_views',
            'max_views',
            'author_username',
            'category_name',
        ]


class CommentFilter(django_filters.FilterSet):
    """
    Custom filter for Comment model.
    """
    
    # Filter by post
    post = django_filters.NumberFilter(field_name='post__id')
    
    # Filter by author
    author = django_filters.NumberFilter(field_name='author__id')
    
    # Filter by approval status
    is_approved = django_filters.BooleanFilter()
    
    # Date range
    created_after = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte'
    )
    created_before = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='lte'
    )
    
    # Content search
    content = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Comment
        fields = [
            'post',
            'author',
            'is_approved',
            'created_after',
            'created_before',
            'content',
        ]
