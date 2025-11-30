"""
Sample Models for Django REST Framework Tutorial
Day 15: Django REST Framework Basics
"""

from django.db import models


class Book(models.Model):
    """
    Book model for our bookstore API
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Author(models.Model):
    """
    Author model with relationship to books
    """
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model for organizing books
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name


class BookWithRelations(models.Model):
    """
    Advanced Book model with ForeignKey and ManyToMany relationships
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books'
    )
    categories = models.ManyToManyField(
        Category, 
        related_name='books',
        blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
