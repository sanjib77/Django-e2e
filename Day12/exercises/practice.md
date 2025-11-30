# Day 12 Practice Exercises

## Exercise 1: Create Models

Create the following models for an e-commerce application:

### Requirements:
1. **Product** model with:
   - `name` (CharField, max 200)
   - `description` (TextField)
   - `price` (DecimalField)
   - `stock` (IntegerField)
   - `created_at` (DateTimeField, auto_now_add)
   - `updated_at` (DateTimeField, auto_now)
   - `is_available` (BooleanField, default True)

2. **Category** model with:
   - `name` (CharField, max 100)
   - `slug` (SlugField, unique)
   - Relationship: One category can have many products

3. Implement `__str__` methods for both models

### Solution:
<details>
<summary>Click to reveal</summary>

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
```
</details>

---

## Exercise 2: ORM Queries

Given the Post model from the blog project, write queries for the following:

1. Get all published posts
2. Get posts by a specific author (username='john')
3. Get posts created in 2024
4. Get posts with more than 100 views
5. Get the 5 most recent posts
6. Count all published posts
7. Get posts containing 'Django' in the title
8. Update all draft posts to published
9. Delete posts with 0 views
10. Get posts with their author information in a single query

### Solution:
<details>
<summary>Click to reveal</summary>

```python
# 1. Get all published posts
posts = Post.objects.filter(status='published')

# 2. Get posts by a specific author
posts = Post.objects.filter(author__username='john')

# 3. Get posts created in 2024
posts = Post.objects.filter(created_at__year=2024)

# 4. Get posts with more than 100 views
posts = Post.objects.filter(views__gt=100)

# 5. Get the 5 most recent posts
posts = Post.objects.order_by('-created_at')[:5]

# 6. Count all published posts
count = Post.objects.filter(status='published').count()

# 7. Get posts containing 'Django' in the title
posts = Post.objects.filter(title__icontains='Django')

# 8. Update all draft posts to published
Post.objects.filter(status='draft').update(status='published')

# 9. Delete posts with 0 views
Post.objects.filter(views=0).delete()

# 10. Get posts with author information in a single query
posts = Post.objects.select_related('author').all()
```
</details>

---

## Exercise 3: Migrations

Answer the following questions:

1. What command creates a new migration file?
2. What command applies migrations to the database?
3. How do you see all migrations and their status?
4. How do you revert to a specific migration?
5. How do you see the SQL that a migration will run?

### Solution:
<details>
<summary>Click to reveal</summary>

```bash
# 1. Create migration
python manage.py makemigrations

# 2. Apply migrations
python manage.py migrate

# 3. See all migrations
python manage.py showmigrations

# 4. Revert to specific migration
python manage.py migrate app_name 0001_initial

# 5. See SQL
python manage.py sqlmigrate app_name 0001
```
</details>

---

## Exercise 4: Admin Customization

Create an admin configuration for the Product model with:

1. `list_display` showing name, price, stock, and is_available
2. `list_filter` for is_available and category
3. `search_fields` for name and description
4. `list_editable` for stock and is_available
5. A custom action to mark products as out of stock

### Solution:
<details>
<summary>Click to reveal</summary>

```python
from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_available', 'category']
    list_filter = ['is_available', 'category']
    search_fields = ['name', 'description']
    list_editable = ['stock', 'is_available']
    actions = ['mark_out_of_stock']
    
    @admin.action(description='Mark selected as out of stock')
    def mark_out_of_stock(self, request, queryset):
        queryset.update(is_available=False, stock=0)
```
</details>

---

## Exercise 5: Build a Mini-Project

Create a simple **Book Library** application with:

### Models:
- **Author**: name, bio, birth_date
- **Book**: title, author (ForeignKey), isbn, published_date, pages, in_stock

### Requirements:
1. Create the models
2. Run migrations
3. Register models in admin with customization
4. Create at least 3 books via Django admin
5. Write 5 different ORM queries to retrieve books

### Bonus:
- Add a ManyToMany relationship for genres
- Add a custom method to check if a book is a "long read" (>500 pages)

---

## Quick Challenge: Fix the Bug

The following code has bugs. Find and fix them:

```python
# Bug 1: Model definition
class Article(models.Model):
    title = models.CharField()  # What's wrong?
    content = models.TextField
    published = models.BooleanField(default='True')  # What's wrong?

# Bug 2: Query
articles = Article.objects.get(published=True)  # What's wrong?

# Bug 3: Update
article = Article.objects.filter(pk=1)
article.title = "New Title"  # What's wrong?
article.save()
```

### Solution:
<details>
<summary>Click to reveal</summary>

```python
# Bug 1 Fixes:
class Article(models.Model):
    title = models.CharField(max_length=200)  # max_length required
    content = models.TextField()  # Need () to call it
    published = models.BooleanField(default=True)  # True not 'True'

# Bug 2 Fix:
# get() returns single object, use filter() for multiple
articles = Article.objects.filter(published=True)
# Or if you want one: article = Article.objects.filter(published=True).first()

# Bug 3 Fix:
# filter() returns QuerySet, not object
article = Article.objects.get(pk=1)  # Use get() for single object
article.title = "New Title"
article.save()
```
</details>

---

## 🎯 Learning Checklist

Before moving on, make sure you can:

- [ ] Create Django models with various field types
- [ ] Understand and use model relationships (ForeignKey, ManyToMany, OneToOne)
- [ ] Run makemigrations and migrate commands
- [ ] Use basic ORM queries (all, get, filter, exclude, create, update, delete)
- [ ] Use field lookups (__contains, __gt, __lt, __isnull, etc.)
- [ ] Set up Django Admin for your models
- [ ] Customize admin with list_display, list_filter, search_fields
- [ ] Create custom admin actions

**Great job! Now take the daily test! 📝**
