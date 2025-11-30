# Django Models

## What are Models?

Models are Python classes that define the structure of your data. Each model maps to a single database table. Django's ORM (Object-Relational Mapping) handles all the database operations for you!

## 🎯 Key Concepts

- **Model** = Database table
- **Field** = Table column
- **Instance** = Table row

## Creating Your First Model

```python
# blog/models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
```

## Common Field Types

| Field Type | Description | Example |
|------------|-------------|---------|
| `CharField` | Short text (requires max_length) | `name = CharField(max_length=100)` |
| `TextField` | Long text (no max_length needed) | `content = TextField()` |
| `IntegerField` | Integer numbers | `age = IntegerField()` |
| `FloatField` | Decimal numbers | `price = FloatField()` |
| `BooleanField` | True/False | `is_active = BooleanField(default=True)` |
| `DateField` | Date only | `birth_date = DateField()` |
| `DateTimeField` | Date and time | `created_at = DateTimeField(auto_now_add=True)` |
| `EmailField` | Email validation | `email = EmailField()` |
| `URLField` | URL validation | `website = URLField()` |
| `ImageField` | Image file | `photo = ImageField(upload_to='images/')` |
| `FileField` | Any file | `document = FileField(upload_to='docs/')` |

## Field Options

```python
class Product(models.Model):
    # Required field with max length
    name = models.CharField(max_length=200)
    
    # Optional field (can be null in DB, blank in forms)
    description = models.TextField(null=True, blank=True)
    
    # Field with default value
    in_stock = models.BooleanField(default=True)
    
    # Unique field
    sku = models.CharField(max_length=50, unique=True)
    
    # Auto timestamp on creation
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Auto timestamp on every save
    updated_at = models.DateTimeField(auto_now=True)
    
    # Choices
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
```

## Relationships

### One-to-Many (ForeignKey)
One author can have many posts:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

### Many-to-Many
A post can have many tags, and a tag can be on many posts:

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
```

### One-to-One
Each user has exactly one profile:

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')
```

## on_delete Options

| Option | Behavior |
|--------|----------|
| `CASCADE` | Delete related objects too |
| `PROTECT` | Prevent deletion if related objects exist |
| `SET_NULL` | Set to NULL (requires `null=True`) |
| `SET_DEFAULT` | Set to default value |
| `DO_NOTHING` | Do nothing (be careful!) |

## The __str__ Method

Always define `__str__` for human-readable representation:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
```

## Model Methods

Add custom methods to your models:

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def get_summary(self, length=100):
        """Return first 100 characters of content"""
        return self.content[:length] + '...' if len(self.content) > length else self.content
    
    def increment_views(self):
        """Increase view count by 1"""
        self.views += 1
        self.save()
```

## Meta Class Options

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # Default ordering
        ordering = ['-created_at']
        
        # Custom table name
        db_table = 'blog_posts'
        
        # Plural name for admin
        verbose_name_plural = 'Posts'
        
        # Unique together constraint
        unique_together = ['title', 'author']
```

## 💡 Quick Tips

1. **Always define `__str__`** - Makes debugging much easier
2. **Use `auto_now_add` for created timestamps** - Sets once on creation
3. **Use `auto_now` for updated timestamps** - Updates on every save
4. **Think about `on_delete` carefully** - CASCADE can delete lots of data!
5. **Use `blank=True, null=True` for optional fields**

## Next Steps

After defining your models, you need to:
1. Make migrations (`python manage.py makemigrations`)
2. Apply migrations (`python manage.py migrate`)

➡️ Continue to [02_migrations.md](02_migrations.md)
