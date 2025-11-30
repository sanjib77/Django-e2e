"""
Day 16: Custom Pagination Classes

Pagination helps manage large datasets efficiently.
"""

from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    CursorPagination
)


class StandardResultsPagination(PageNumberPagination):
    """
    Standard pagination with configurable page size.
    
    - Default: 10 items per page
    - Client can request up to 100 items per page
    - Uses 'page' query parameter
    
    Usage:
        GET /api/posts/                # First page, 10 items
        GET /api/posts/?page=2         # Second page
        GET /api/posts/?page_size=25   # Custom page size
    """
    
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class SmallResultsPagination(PageNumberPagination):
    """
    Smaller pagination for lists that should load quickly.
    
    - Default: 5 items per page
    - Max: 20 items per page
    """
    
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class LargeResultsPagination(PageNumberPagination):
    """
    Larger pagination for admin or batch operations.
    
    - Default: 50 items per page
    - Max: 500 items per page
    """
    
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class FlexibleLimitOffsetPagination(LimitOffsetPagination):
    """
    Limit-offset pagination for more flexible navigation.
    
    Usage:
        GET /api/posts/?limit=20        # First 20 items
        GET /api/posts/?limit=20&offset=40  # Items 41-60
    """
    
    default_limit = 10
    max_limit = 100


class CommentCursorPagination(CursorPagination):
    """
    Cursor-based pagination for comments.
    
    Best for:
    - Real-time data
    - Consistent results even when data changes
    - Very large datasets
    
    Note: Only works with fields that have database indexes.
    """
    
    page_size = 10
    ordering = '-created_at'
    cursor_query_param = 'cursor'
