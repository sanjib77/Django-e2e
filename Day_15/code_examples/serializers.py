"""
Serializers for Django REST Framework Tutorial
Day 15: Django REST Framework Basics
"""

from rest_framework import serializers
from .models import Book, Author, Category, BookWithRelations


# =============================================================================
# BASIC MODEL SERIALIZER
# =============================================================================

class BookSerializer(serializers.ModelSerializer):
    """
    Basic serializer for Book model.
    Automatically creates fields from the model.
    """
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields


class BookListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing books (fewer fields for performance)
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'in_stock']


# =============================================================================
# SERIALIZER WITH VALIDATION
# =============================================================================

class BookCreateSerializer(serializers.ModelSerializer):
    """
    Serializer with custom validation
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'isbn', 'published_date']
    
    def validate_price(self, value):
        """
        Check that price is positive
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number")
        return value
    
    def validate_isbn(self, value):
        """
        Check that ISBN is valid (13 digits)
        """
        if not value.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits")
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be exactly 13 digits")
        return value
    
    def validate(self, data):
        """
        Object-level validation
        """
        # Example: Check title and author are different
        if data.get('title', '').lower() == data.get('author', '').lower():
            raise serializers.ValidationError({
                "title": "Title cannot be the same as author name"
            })
        return data


# =============================================================================
# SERIALIZER WITH CUSTOM FIELDS
# =============================================================================

class BookDetailSerializer(serializers.ModelSerializer):
    """
    Serializer with computed fields
    """
    # Read-only computed field
    discounted_price = serializers.SerializerMethodField()
    # Rename field for output
    stock_status = serializers.BooleanField(source='in_stock', read_only=True)
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'description', 
            'price', 'discounted_price', 'stock_status',
            'published_date', 'isbn', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_discounted_price(self, obj):
        """
        Calculate 10% discount
        """
        return round(float(obj.price) * 0.9, 2)


# =============================================================================
# NESTED SERIALIZERS
# =============================================================================

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_date', 'email']


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for Category model
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookWithRelationsSerializer(serializers.ModelSerializer):
    """
    Serializer with nested relationships
    """
    # Nested serializer (read-only by default)
    author = AuthorSerializer(read_only=True)
    # For writing, accept author ID
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    # Nested many relationship
    categories = CategorySerializer(many=True, read_only=True)
    # For writing, accept category IDs
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='categories',
        write_only=True,
        many=True,
        required=False
    )
    
    class Meta:
        model = BookWithRelations
        fields = [
            'id', 'title', 
            'author', 'author_id',
            'categories', 'category_ids',
            'price', 'in_stock'
        ]


# =============================================================================
# NON-MODEL SERIALIZER (for custom data)
# =============================================================================

class BookSearchSerializer(serializers.Serializer):
    """
    Serializer for search parameters (not tied to a model)
    """
    query = serializers.CharField(max_length=200)
    min_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, required=False
    )
    max_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, required=False
    )
    in_stock_only = serializers.BooleanField(default=False)
    
    def validate(self, data):
        """
        Check that min_price is less than max_price
        """
        min_price = data.get('min_price')
        max_price = data.get('max_price')
        
        if min_price and max_price and min_price > max_price:
            raise serializers.ValidationError({
                "min_price": "min_price must be less than max_price"
            })
        return data
