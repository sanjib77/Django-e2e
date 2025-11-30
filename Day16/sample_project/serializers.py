"""
Day 16: DRF Serializers for Blog API

Serializers convert model instances to JSON and validate input data.
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model (read-only, for nested display)."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = fields


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    
    post_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'post_count', 'created_at']
        read_only_fields = ['created_at']
    
    def get_post_count(self, obj):
        return obj.posts.count()


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at', 'is_approved']
        read_only_fields = ['author', 'created_at', 'updated_at']


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for listing posts (less detail)."""
    
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'author', 'category',
            'status', 'views', 'comment_count', 'created_at'
        ]
    
    def get_comment_count(self, obj):
        return obj.comments.count()


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for detailed post view."""
    
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'author',
            'category', 'status', 'views', 'comments',
            'created_at', 'updated_at', 'published_at'
        ]
        read_only_fields = ['author', 'views', 'created_at', 'updated_at']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating posts."""
    
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'content', 'excerpt',
            'category', 'status', 'published_at'
        ]
    
    def validate_slug(self, value):
        """Ensure slug is URL-friendly."""
        if not value.replace('-', '').isalnum():
            raise serializers.ValidationError(
                "Slug must contain only letters, numbers, and hyphens."
            )
        return value.lower()
