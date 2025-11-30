# Serializers in Django REST Framework

## 🔄 What is a Serializer?

A **serializer** converts complex data types (like Django models) into Python data types that can be easily rendered into JSON, XML, or other content types. It also works in reverse - **deserializing** incoming data back into complex types.

```
Django Model ←→ Serializer ←→ JSON
     │                         │
   Python                  API Response
   Object                  (or Request)
```

## 🎯 Why Serializers?

| Without Serializers | With Serializers |
|--------------------|------------------|
| Manual conversion code | Automatic conversion |
| No validation | Built-in validation |
| Error-prone | Consistent & reliable |
| Lots of boilerplate | Clean, DRY code |

## 📝 Creating Your First Serializer

### Step 1: Define Your Model

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
```

### Step 2: Create the Serializer

```python
# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Include all fields
```

That's it! DRF handles the rest.

## 🔍 Types of Serializers

### 1. ModelSerializer (Most Common)

Automatically creates fields based on your model:

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # All fields
        
        # OR specify fields explicitly
        # fields = ['id', 'title', 'author', 'price']
        
        # OR exclude certain fields
        # exclude = ['isbn']
```

### 2. Basic Serializer

For custom scenarios or non-model data:

```python
class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    published_date = serializers.DateField()
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
```

## 💡 Using Serializers

### Serialization (Object → JSON)

```python
# Get a book from database
book = Book.objects.get(id=1)

# Serialize it
serializer = BookSerializer(book)

# Access the data
print(serializer.data)
# Output: {'id': 1, 'title': 'Django for Beginners', 'author': 'William Vincent', ...}
```

### Serializing Multiple Objects

```python
books = Book.objects.all()
serializer = BookSerializer(books, many=True)  # Note: many=True
print(serializer.data)
# Output: [{'id': 1, ...}, {'id': 2, ...}, ...]
```

### Deserialization (JSON → Object)

```python
# Incoming data (from API request)
data = {
    'title': 'New Book',
    'author': 'John Doe',
    'price': '29.99',
    'published_date': '2024-01-15',
    'isbn': '1234567890123'
}

# Create serializer with data
serializer = BookSerializer(data=data)

# Validate
if serializer.is_valid():
    book = serializer.save()  # Creates new Book in database
    print(book.id)  # Prints the new book's ID
else:
    print(serializer.errors)  # Shows validation errors
```

### Updating an Object

```python
book = Book.objects.get(id=1)
data = {'price': '39.99'}

serializer = BookSerializer(book, data=data, partial=True)  # partial=True for PATCH
if serializer.is_valid():
    serializer.save()
```

## ✅ Validation

### Built-in Validation

DRF automatically validates based on model fields:

```python
# This will fail - price can't have 3 decimal places
data = {'price': '29.999', ...}
serializer = BookSerializer(data=data)
serializer.is_valid()  # False
print(serializer.errors)  
# {'price': ['Ensure that there are no more than 2 decimal places.']}
```

### Field-Level Validation

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_price(self, value):
        """Price must be positive"""
        if value < 0:
            raise serializers.ValidationError("Price must be positive")
        return value
    
    def validate_isbn(self, value):
        """ISBN must be 13 characters"""
        if len(value) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters")
        return value
```

### Object-Level Validation

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, data):
        """
        Check that published_date is in the past
        """
        from datetime import date
        if data.get('published_date') and data['published_date'] > date.today():
            raise serializers.ValidationError({
                "published_date": "Published date cannot be in the future"
            })
        return data
```

## 🎨 Custom Fields

### Read-Only Fields

```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
```

### Computed/Method Fields

```python
class BookSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'discounted_price']
    
    def get_discounted_price(self, obj):
        """10% discount"""
        return float(obj.price) * 0.9
```

### Nested Serializers

```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # Nested!
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

## 📊 Serializer Comparison

| Feature | Serializer | ModelSerializer |
|---------|------------|-----------------|
| Field definitions | Manual | Automatic |
| create() method | Manual | Automatic |
| update() method | Manual | Automatic |
| Validation | Manual | Automatic |
| Use case | Custom/non-model | Model-based |

## 💪 Practice Exercise

Create a serializer for this model:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

Requirements:
1. Include all fields except `created_at` in the response
2. Make `id` read-only
3. Validate that `price` is positive
4. Validate that `stock` is not negative

<details>
<summary>Solution</summary>

```python
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at']
        read_only_fields = ['id']
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be positive")
        return value
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return value
```
</details>

---

**Next:** [Views and ViewSets](./04_views_and_viewsets.md)
