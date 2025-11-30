# Django ORM Queries

## What is the ORM?

ORM (Object-Relational Mapping) lets you interact with your database using Python code instead of SQL. Django's ORM is powerful, intuitive, and handles SQL injection protection automatically!

## 🎯 Key Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `all()` | QuerySet | All objects |
| `get()` | Object | Single object |
| `filter()` | QuerySet | Filtered objects |
| `exclude()` | QuerySet | Objects NOT matching |
| `create()` | Object | Create and save |
| `first()` | Object/None | First object |
| `last()` | Object/None | Last object |
| `count()` | Integer | Number of objects |

## Setting Up (Django Shell)

```bash
# Open Django interactive shell
python manage.py shell

# Import your models
>>> from blog.models import Post
>>> from django.contrib.auth.models import User
```

## CRUD Operations

### CREATE - Adding Objects

```python
# Method 1: Create and save separately
post = Post(title="My First Post", content="Hello World!")
post.author = user
post.save()

# Method 2: Create and save in one step
post = Post.objects.create(
    title="My Second Post",
    content="This is easier!",
    author=user
)

# Method 3: get_or_create (avoid duplicates)
post, created = Post.objects.get_or_create(
    title="Unique Post",
    defaults={'content': 'Default content', 'author': user}
)
# created is True if new, False if existing
```

### READ - Retrieving Objects

```python
# Get ALL objects
posts = Post.objects.all()

# Get SINGLE object (raises exception if not found or multiple)
post = Post.objects.get(id=1)
post = Post.objects.get(pk=1)  # pk = primary key

# Get FIRST object
post = Post.objects.first()

# Get LAST object
post = Post.objects.last()

# Count objects
count = Post.objects.count()

# Check if exists
exists = Post.objects.filter(title="Hello").exists()
```

### UPDATE - Modifying Objects

```python
# Method 1: Get, modify, save
post = Post.objects.get(pk=1)
post.title = "Updated Title"
post.save()

# Method 2: Update multiple objects
Post.objects.filter(published=False).update(published=True)

# Method 3: update_or_create
post, created = Post.objects.update_or_create(
    id=1,
    defaults={'title': 'New Title', 'content': 'New Content'}
)
```

### DELETE - Removing Objects

```python
# Delete single object
post = Post.objects.get(pk=1)
post.delete()

# Delete multiple objects
Post.objects.filter(published=False).delete()

# Delete ALL objects (dangerous!)
Post.objects.all().delete()
```

## Filtering Queries

### Basic Filtering

```python
# Exact match
posts = Post.objects.filter(title="Hello World")

# Multiple conditions (AND)
posts = Post.objects.filter(published=True, author=user)

# Chain filters
posts = Post.objects.filter(published=True).filter(author=user)
```

### Field Lookups

```python
# Contains (case-sensitive)
posts = Post.objects.filter(title__contains="Django")

# Contains (case-insensitive)
posts = Post.objects.filter(title__icontains="django")

# Starts with
posts = Post.objects.filter(title__startswith="How to")

# Ends with
posts = Post.objects.filter(title__endswith="Python")

# Exact match
posts = Post.objects.filter(title__exact="Hello World")

# Case-insensitive exact
posts = Post.objects.filter(title__iexact="hello world")
```

### Comparison Lookups

```python
# Greater than
posts = Post.objects.filter(views__gt=100)

# Greater than or equal
posts = Post.objects.filter(views__gte=100)

# Less than
posts = Post.objects.filter(views__lt=50)

# Less than or equal
posts = Post.objects.filter(views__lte=50)

# In a list
posts = Post.objects.filter(id__in=[1, 2, 3])

# Range
posts = Post.objects.filter(views__range=(10, 100))
```

### Date Lookups

```python
# By year
posts = Post.objects.filter(created_at__year=2024)

# By month
posts = Post.objects.filter(created_at__month=12)

# By day
posts = Post.objects.filter(created_at__day=25)

# Date range
from datetime import date
start_date = date(2024, 1, 1)
end_date = date(2024, 12, 31)
posts = Post.objects.filter(created_at__date__range=[start_date, end_date])
```

### Null Checks

```python
# Is null
posts = Post.objects.filter(author__isnull=True)

# Is not null
posts = Post.objects.filter(author__isnull=False)
```

## Excluding Results

```python
# Exclude certain results
posts = Post.objects.exclude(published=False)

# Combine with filter
posts = Post.objects.filter(author=user).exclude(published=False)
```

## Ordering Results

```python
# Ascending
posts = Post.objects.order_by('created_at')

# Descending
posts = Post.objects.order_by('-created_at')

# Multiple fields
posts = Post.objects.order_by('-published', 'title')

# Random order
posts = Post.objects.order_by('?')
```

## Limiting Results

```python
# First 5
posts = Post.objects.all()[:5]

# 5 to 10
posts = Post.objects.all()[5:10]

# Every other post
posts = Post.objects.all()[::2]
```

## Aggregation

```python
from django.db.models import Count, Avg, Max, Min, Sum

# Count
total = Post.objects.count()
published_count = Post.objects.filter(published=True).count()

# Aggregations
from django.db.models import Avg, Sum, Max, Min
result = Post.objects.aggregate(
    avg_views=Avg('views'),
    total_views=Sum('views'),
    max_views=Max('views'),
    min_views=Min('views')
)
```

## Related Objects

### Forward Relationships (ForeignKey)

```python
# Get related object
post = Post.objects.get(pk=1)
author = post.author  # Gets the User object
author_name = post.author.username
```

### Reverse Relationships

```python
# Get all posts by an author
user = User.objects.get(username='john')
posts = user.post_set.all()  # Default related name

# With custom related_name
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

# Now use:
posts = user.posts.all()
```

### Filtering by Related Objects

```python
# Posts by author username
posts = Post.objects.filter(author__username='john')

# Posts by author email domain
posts = Post.objects.filter(author__email__endswith='@gmail.com')
```

## Q Objects (Complex Queries)

For OR conditions and complex queries:

```python
from django.db.models import Q

# OR condition
posts = Post.objects.filter(
    Q(title__contains='Django') | Q(title__contains='Python')
)

# NOT condition
posts = Post.objects.filter(~Q(published=False))

# Complex combination
posts = Post.objects.filter(
    Q(author=user) & (Q(published=True) | Q(featured=True))
)
```

## F Objects (Field References)

Reference field values in queries:

```python
from django.db.models import F

# Compare two fields
posts = Post.objects.filter(views__gt=F('comments_count'))

# Update with field reference
Post.objects.update(views=F('views') + 1)

# Mathematical operations
Post.objects.update(score=F('likes') - F('dislikes'))
```

## QuerySet Methods Chaining

```python
# Chain multiple methods
posts = Post.objects.filter(published=True) \
                    .exclude(author__isnull=True) \
                    .order_by('-created_at') \
                    .select_related('author')[:10]
```

## Performance Optimization

### select_related (for ForeignKey)
```python
# Without: N+1 queries
posts = Post.objects.all()
for post in posts:
    print(post.author.username)  # Each hit makes a query!

# With: 1 query (JOIN)
posts = Post.objects.select_related('author')
for post in posts:
    print(post.author.username)  # No extra queries!
```

### prefetch_related (for ManyToMany)
```python
# Efficiently fetch related many-to-many
posts = Post.objects.prefetch_related('tags')
```

## Common Patterns

```python
# Get or 404 (in views)
from django.shortcuts import get_object_or_404
post = get_object_or_404(Post, pk=post_id)

# Check if exists
if Post.objects.filter(title="Test").exists():
    print("Found!")

# Get values only (not full objects)
titles = Post.objects.values_list('title', flat=True)

# Distinct results
unique_authors = Post.objects.values('author').distinct()
```

## 💡 Quick Tips

1. **Use `get()` only when you expect exactly one result**
2. **QuerySets are lazy** - they don't hit the database until evaluated
3. **Use `select_related` for ForeignKey** to avoid N+1 queries
4. **Use `prefetch_related` for ManyToMany** relationships
5. **Chain methods** for complex queries
6. **Use `values()` or `values_list()`** when you only need specific fields

➡️ Continue to [04_admin.md](04_admin.md)
