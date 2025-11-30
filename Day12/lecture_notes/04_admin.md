# Django Admin Setup

## What is Django Admin?

Django Admin is a powerful built-in interface for managing your application's data. It's automatically generated from your models and is fully customizable!

## 🎯 Key Features

- ✅ Automatic CRUD interface for models
- ✅ User authentication and permissions
- ✅ Search, filter, and sort functionality
- ✅ Bulk actions
- ✅ Fully customizable

## Setting Up Admin

### Step 1: Create Superuser

```bash
python manage.py createsuperuser
```

You'll be prompted for:
- Username
- Email address
- Password (entered twice)

### Step 2: Register Your Models

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Step 3: Access Admin

Run the server and go to: `http://127.0.0.1:8000/admin/`

## Customizing Admin

### Basic Customization with ModelAdmin

```python
# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Fields to display in list view
    list_display = ['title', 'author', 'created_at', 'published']
    
    # Fields to filter by (sidebar)
    list_filter = ['published', 'created_at', 'author']
    
    # Fields to search
    search_fields = ['title', 'content']
    
    # Default ordering
    ordering = ['-created_at']
    
    # Number of items per page
    list_per_page = 25
```

### Date Hierarchy

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    date_hierarchy = 'created_at'  # Adds date drill-down navigation
```

### Editable Fields in List View

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published']
    list_editable = ['published']  # Edit directly in list view!
```

### Display Links

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published']
    list_display_links = ['title', 'author']  # Click to edit
```

## Customizing the Form View

### Fieldsets

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', {
            'fields': ['title', 'content']
        }),
        ('Publishing', {
            'fields': ['author', 'published', 'created_at'],
            'classes': ['collapse']  # Collapsible section
        }),
    ]
```

### Read-Only Fields

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
```

### Prepopulated Fields

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Auto-fill slug from title
```

### Exclude Fields

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ['views']  # Hide from admin form
```

## Custom Actions

### Simple Action

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
    actions = ['make_published', 'make_unpublished']
    
    @admin.action(description='Mark selected posts as published')
    def make_published(self, request, queryset):
        queryset.update(published=True)
    
    @admin.action(description='Mark selected posts as unpublished')
    def make_unpublished(self, request, queryset):
        queryset.update(published=False)
```

### Action with Message

```python
from django.contrib import messages

@admin.action(description='Mark selected posts as published')
def make_published(self, request, queryset):
    updated = queryset.update(published=True)
    self.message_user(
        request,
        f'{updated} posts were marked as published.',
        messages.SUCCESS
    )
```

## Inline Models

Edit related models on the same page:

```python
# blog/models.py
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# blog/admin.py
class CommentInline(admin.TabularInline):  # or admin.StackedInline
    model = Comment
    extra = 1  # Number of empty forms to display

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    inlines = [CommentInline]
```

## Custom Display Methods

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'short_content', 'is_recent']
    
    @admin.display(description='Content Preview')
    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    
    @admin.display(boolean=True, description='Recent?')
    def is_recent(self, obj):
        from django.utils import timezone
        from datetime import timedelta
        return obj.created_at >= timezone.now() - timedelta(days=7)
```

## Filtering QuerySets

### Custom Queryset

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
```

### Custom List Filter

```python
class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade'
    parameter_name = 'decade'
    
    def lookups(self, request, model_admin):
        return (
            ('2020s', '2020s'),
            ('2010s', '2010s'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == '2020s':
            return queryset.filter(created_at__year__gte=2020)
        if self.value() == '2010s':
            return queryset.filter(
                created_at__year__gte=2010,
                created_at__year__lt=2020
            )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = [DecadeListFilter, 'published']
```

## Admin Site Customization

### Custom Admin Header

```python
# blog/admin.py
admin.site.site_header = "My Blog Admin"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to the Blog Admin Portal"
```

## Full Example

```python
# blog/admin.py
from django.contrib import admin
from django.contrib import messages
from .models import Post, Category, Tag

admin.site.site_header = "My Blog Admin"
admin.site.site_title = "Blog Admin"
admin.site.index_title = "Welcome to Blog Administration"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}
    
    @admin.display(description='Posts')
    def post_count(self, obj):
        return obj.posts.count()

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published', 'created_at']
    list_filter = ['published', 'category', 'created_at']
    list_editable = ['published']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    
    fieldsets = [
        ('Content', {
            'fields': ['title', 'slug', 'content']
        }),
        ('Metadata', {
            'fields': ['author', 'category', 'tags']
        }),
        ('Publishing', {
            'fields': ['published', 'created_at'],
            'classes': ['collapse']
        }),
    ]
    
    readonly_fields = ['created_at']
    filter_horizontal = ['tags']  # Nice widget for ManyToMany
    
    actions = ['publish_posts', 'unpublish_posts']
    
    @admin.action(description='Publish selected posts')
    def publish_posts(self, request, queryset):
        count = queryset.update(published=True)
        self.message_user(request, f'{count} posts published.', messages.SUCCESS)
    
    @admin.action(description='Unpublish selected posts')
    def unpublish_posts(self, request, queryset):
        count = queryset.update(published=False)
        self.message_user(request, f'{count} posts unpublished.', messages.WARNING)
```

## 💡 Quick Tips

1. **Use `@admin.register` decorator** instead of `admin.site.register()`
2. **Add `list_display`** for better list view
3. **Add `search_fields`** for searchable content
4. **Add `list_filter`** for quick filtering
5. **Use `prepopulated_fields`** for slugs
6. **Use `fieldsets`** to organize form fields
7. **Use `inlines`** for related models
8. **Create custom actions** for bulk operations

## Admin URL

The admin is available at `/admin/` by default (configured in `urls.py`):

```python
# project/urls.py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... your other URLs
]
```

## Next Steps

Now you know how to:
- Create models
- Run migrations
- Use ORM queries
- Set up admin

Time to build something! ➡️ Check out the blog project in `../blog_project/`
