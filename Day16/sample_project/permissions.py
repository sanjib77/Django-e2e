"""
Day 16: Custom Permission Classes

Permission classes control who can access what in your API.
"""

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    
    - Anyone can read (GET, HEAD, OPTIONS)
    - Only the owner can modify (POST, PUT, PATCH, DELETE)
    
    Usage:
        class MyViewSet(viewsets.ModelViewSet):
            permission_classes = [IsOwnerOrReadOnly]
    
    Note: The model must have an 'author' field that references the User model.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        # Adjust 'author' to match your model's owner field
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission that allows:
    - Anyone to read (GET, HEAD, OPTIONS)
    - Only admin users to modify (POST, PUT, PATCH, DELETE)
    
    Usage:
        class CategoryViewSet(viewsets.ModelViewSet):
            permission_classes = [IsAdminOrReadOnly]
    """

    def has_permission(self, request, view):
        # Allow read access for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write access only for admin users
        return request.user and request.user.is_staff


class IsAuthenticatedOrReadOnlyForList(permissions.BasePermission):
    """
    Custom permission that allows:
    - Anyone to list and retrieve
    - Only authenticated users to create, update, delete
    
    This is more granular than IsAuthenticatedOrReadOnly.
    """

    def has_permission(self, request, view):
        # Allow list and retrieve for everyone
        if view.action in ['list', 'retrieve']:
            return True

        # Require authentication for other actions
        return request.user and request.user.is_authenticated


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission that allows:
    - Owners to access their own objects
    - Admin users to access any object
    """

    def has_object_permission(self, request, view, obj):
        # Admin users can do anything
        if request.user and request.user.is_staff:
            return True

        # Owners can access their own objects
        return obj.author == request.user


class IsCommentAuthorOrPostAuthor(permissions.BasePermission):
    """
    Custom permission for comments:
    - Comment author can modify their comment
    - Post author can delete comments on their post
    - Everyone can read
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Comment author can modify
        if obj.author == request.user:
            return True

        # Post author can delete comments (but not modify)
        if request.method == 'DELETE' and obj.post.author == request.user:
            return True

        return False
