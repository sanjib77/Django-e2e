# Day 12 Assessment - Django Models & ORM

## 📋 Test Information
- **Total Points**: 14
- **Passing Score**: 10 points (70%)
- **Time Limit**: 15 minutes
- **Format**: 6 MCQs (1 pt each) + 3 Coding (2 pts each) + 1 Conceptual (2 pts)

---

## Part A: Multiple Choice Questions (6 points)

### Question 1 (1 point)
Which Django command creates migration files based on model changes?

A) `python manage.py migrate`  
B) `python manage.py makemigrations`  
C) `python manage.py runmigrations`  
D) `python manage.py createdb`

---

### Question 2 (1 point)
What is the correct way to define a CharField in Django?

A) `title = models.CharField()`  
B) `title = models.CharField(max_length=200)`  
C) `title = CharField(200)`  
D) `title = models.Text(max_length=200)`

---

### Question 3 (1 point)
Which ORM method returns a single object and raises an exception if not found?

A) `Model.objects.filter()`  
B) `Model.objects.all()`  
C) `Model.objects.get()`  
D) `Model.objects.first()`

---

### Question 4 (1 point)
What does `on_delete=models.CASCADE` do in a ForeignKey relationship?

A) Prevents deletion of related objects  
B) Sets the foreign key to NULL when the related object is deleted  
C) Deletes related objects when the parent object is deleted  
D) Does nothing when the parent object is deleted

---

### Question 5 (1 point)
How do you filter posts created in 2024 using Django ORM?

A) `Post.objects.filter(created_at=2024)`  
B) `Post.objects.filter(created_at__year=2024)`  
C) `Post.objects.get(year=2024)`  
D) `Post.objects.filter(date__year=2024)`

---

### Question 6 (1 point)
Which decorator is used to register a model with a custom ModelAdmin in Django admin?

A) `@admin.model()`  
B) `@admin.site.register`  
C) `@admin.register()`  
D) `@register.admin()`

---

## Part B: Coding Challenges (6 points)

### Question 7 (2 points)
Write a Django model for a `Book` with the following fields:
- `title`: string, max 200 characters
- `author`: string, max 100 characters
- `published_date`: date field
- `price`: decimal field with 2 decimal places
- `in_stock`: boolean, default True

Include the `__str__` method to return the book title.

```python
# Write your code here:
from django.db import models

class Book(models.Model):
    # Your code here
    pass
```

---

### Question 8 (2 points)
Write Django ORM queries for the following operations (assume a `Product` model with fields: `name`, `price`, `stock`, `is_available`):

```python
# 1. Get all available products with price less than $50


# 2. Update all products with stock=0 to set is_available=False


# 3. Get products sorted by price (highest first), limited to 10 results


# 4. Count products that are available


```

---

### Question 9 (2 points)
Write an admin configuration for the `Book` model that includes:
- Display columns: title, author, price, in_stock
- Filter by: in_stock
- Search by: title, author
- Editable in list: in_stock

```python
# Write your code here:
from django.contrib import admin
from .models import Book

# Your code here
```

---

## Part C: Conceptual Question (2 points)

### Question 10 (2 points)
Explain the difference between `filter()` and `get()` in Django ORM. When would you use each? What happens if no matching records are found for each method?

```
Your answer:




```

---

## Answer Key (For Instructor Use)

<details>
<summary>Click to reveal answers</summary>

### Part A Answers:
1. **B** - `python manage.py makemigrations`
2. **B** - `title = models.CharField(max_length=200)`
3. **C** - `Model.objects.get()`
4. **C** - Deletes related objects when the parent object is deleted
5. **B** - `Post.objects.filter(created_at__year=2024)`
6. **C** - `@admin.register()`

### Part B Answers:

**Question 7:**
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
```

**Question 8:**
```python
# 1. Get all available products with price less than $50
products = Product.objects.filter(is_available=True, price__lt=50)

# 2. Update all products with stock=0 to set is_available=False
Product.objects.filter(stock=0).update(is_available=False)

# 3. Get products sorted by price (highest first), limited to 10 results
products = Product.objects.order_by('-price')[:10]

# 4. Count products that are available
count = Product.objects.filter(is_available=True).count()
```

**Question 9:**
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['title', 'author']
    list_editable = ['in_stock']
```

**Question 10:**
- `filter()` returns a QuerySet (list-like) of all matching objects. If no matches found, returns empty QuerySet.
- `get()` returns a single object. Raises `DoesNotExist` if not found, `MultipleObjectsReturned` if more than one found.
- Use `filter()` when expecting multiple results or zero results
- Use `get()` when you need exactly one object (like by primary key)

</details>

---

## Scoring Guide

| Section | Questions | Points |
|---------|-----------|--------|
| Part A | 6 MCQs | 6 |
| Part B | 3 Coding | 6 |
| Part C | 1 Conceptual | 2 |
| **Total** | **10** | **14** |

**Passing Score: 10/14 (70%)**

### Scoring Criteria:
- Part A: 1 point each (correct answer only)
- Part B: 2 points each (full marks for working code, 1 point for partial/minor errors)
- Part C: 2 points for complete explanation, 1 point for partial

---

## 📊 Your Score: ___ / 14

### Result:
- [ ] **PASS** (10+ points) - Proceed to Day 13!
- [ ] **RETRY** (Below 10 points) - Review materials and retake tomorrow

---

## 💡 Study Tips if You Need to Retry

1. Review the lecture notes, especially the examples
2. Practice more ORM queries in Django shell (`python manage.py shell`)
3. Create a small project and experiment with different model configurations
4. Read the Django documentation on Models and QuerySets

**Keep going! You've got this! 💪**
