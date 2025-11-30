# Database Migrations

## What are Migrations?

Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. Think of migrations as **version control for your database**.

## 🎯 Key Concepts

- **Migration** = A file that describes changes to make to the database
- **makemigrations** = Creates new migration files based on model changes
- **migrate** = Applies migrations to the database

## The Migration Workflow

```
1. Make changes to models.py
         ↓
2. Run: python manage.py makemigrations
         ↓
3. Migration file is created
         ↓
4. Run: python manage.py migrate
         ↓
5. Database is updated!
```

## Basic Migration Commands

### Create Migrations
```bash
# Create migrations for all apps
python manage.py makemigrations

# Create migrations for specific app
python manage.py makemigrations blog

# Create migrations with custom name
python manage.py makemigrations blog --name added_published_field
```

### Apply Migrations
```bash
# Apply all pending migrations
python manage.py migrate

# Apply migrations for specific app
python manage.py migrate blog

# Migrate to a specific migration
python manage.py migrate blog 0001_initial
```

### View Migrations
```bash
# Show all migrations and their status
python manage.py showmigrations

# Show migrations for specific app
python manage.py showmigrations blog
```

### SQL Preview
```bash
# Show SQL that would be run
python manage.py sqlmigrate blog 0001
```

## Migration Example

### Step 1: Create Initial Model

```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

### Step 2: Make Migrations

```bash
$ python manage.py makemigrations blog

Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

### Step 3: View the Migration File

```python
# blog/migrations/0001_initial.py
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
```

### Step 4: Apply Migration

```bash
$ python manage.py migrate blog

Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0001_initial... OK
```

## Adding a Field

### Update Model

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # NEW!
```

### Create Migration

```bash
$ python manage.py makemigrations blog

Migrations for 'blog':
  blog/migrations/0002_post_created_at.py
    - Add field created_at to post
```

### Apply Migration

```bash
$ python manage.py migrate blog
```

## Handling Data Migrations

When adding a non-nullable field to a model with existing data:

```bash
$ python manage.py makemigrations blog

You are trying to add a non-nullable field 'author' to post without a default...
Please select a fix:
 1) Provide a one-off default now
 2) Quit, and let me add a default in models.py
Select an option:
```

### Options:

**Option 1: Provide one-off default**
```python
# Django will ask you to provide a value
# Good for simple fields like numbers or strings
```

**Option 2: Add default in model**
```python
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # OR
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
```

## Reverting Migrations

```bash
# Revert to a previous migration
python manage.py migrate blog 0001_initial

# Revert all migrations for an app
python manage.py migrate blog zero
```

⚠️ **Warning**: Be careful when reverting migrations - it can cause data loss!

## Data Migrations

Sometimes you need to migrate data, not just schema:

```python
# blog/migrations/0003_populate_slugs.py
from django.db import migrations
from django.utils.text import slugify

def generate_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.slug = slugify(post.title)
        post.save()

def reverse_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Post.objects.all().update(slug='')

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RunPython(generate_slugs, reverse_slugs),
    ]
```

## Migration Files Structure

```
blog/
└── migrations/
    ├── __init__.py
    ├── 0001_initial.py
    ├── 0002_post_created_at.py
    └── 0003_post_author.py
```

## Common Migration Issues

### 1. Conflicting Migrations
Multiple developers creating migrations at the same time:

```bash
# Merge migrations
python manage.py makemigrations --merge
```

### 2. Missing Migrations
```bash
# Check for unapplied migrations
python manage.py showmigrations

# Look for migrations not yet applied (marked with [ ])
```

### 3. Fake Migrations
When your database is already in the right state:

```bash
# Mark migration as applied without running it
python manage.py migrate blog --fake

# Fake to initial state
python manage.py migrate blog zero --fake
```

## Best Practices

1. **Always run `makemigrations` after model changes**
2. **Review migration files before applying**
3. **Commit migration files to version control**
4. **Never edit migrations after they've been applied**
5. **Use meaningful names for migrations**
6. **Test migrations in development before production**

## Quick Reference

| Command | Description |
|---------|-------------|
| `makemigrations` | Create new migration files |
| `migrate` | Apply pending migrations |
| `showmigrations` | List all migrations |
| `sqlmigrate app 0001` | Show SQL for a migration |
| `migrate app zero` | Revert all migrations for app |
| `migrate --fake` | Mark as applied without running |

## 💡 Quick Tips

1. **Never delete migration files** unless you know what you're doing
2. **Run migrations in a specific order** on production servers
3. **Use `--dry-run`** to see what would happen without making changes
4. **Squash migrations** when you have too many (`squashmigrations` command)

➡️ Continue to [03_orm_queries.md](03_orm_queries.md)
