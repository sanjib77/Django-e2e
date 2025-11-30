from django.contrib import admin
from django.contrib import messages
from .models import Post, Category, Tag, Comment


# Customize admin site header
admin.site.site_header = "Blog Administration"
admin.site.site_title = "Blog Admin Portal"
admin.site.index_title = "Welcome to the Blog Admin Portal"


class CommentInline(admin.TabularInline):
    """Inline admin for comments on posts."""
    model = Comment
    extra = 0
    readonly_fields = ['created_at']
    fields = ['author_name', 'author_email', 'content', 'approved', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model."""
    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

    @admin.display(description='Posts')
    def post_count(self, obj):
        return obj.posts.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin configuration for Tag model."""
    list_display = ['name', 'post_count']
    search_fields = ['name']

    @admin.display(description='Posts')
    def post_count(self, obj):
        return obj.posts.count()


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin configuration for Post model."""
    list_display = ['title', 'author', 'category', 'status', 'views', 'created_at', 'is_recent']
    list_filter = ['status', 'category', 'created_at', 'author']
    list_editable = ['status']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 20
    filter_horizontal = ['tags']
    raw_id_fields = ['author']
    readonly_fields = ['views', 'created_at', 'updated_at']

    fieldsets = [
        ('Content', {
            'fields': ['title', 'slug', 'content', 'excerpt', 'featured_image']
        }),
        ('Metadata', {
            'fields': ['author', 'category', 'tags']
        }),
        ('Publishing', {
            'fields': ['status', 'published_at'],
            'classes': ['collapse']
        }),
        ('Statistics', {
            'fields': ['views', 'created_at', 'updated_at'],
            'classes': ['collapse']
        }),
    ]

    inlines = [CommentInline]
    actions = ['publish_posts', 'unpublish_posts', 'reset_views']

    @admin.display(boolean=True, description='Recent?')
    def is_recent(self, obj):
        from django.utils import timezone
        from datetime import timedelta
        return obj.created_at >= timezone.now() - timedelta(days=7)

    @admin.action(description='Publish selected posts')
    def publish_posts(self, request, queryset):
        from django.utils import timezone
        count = queryset.update(status='published', published_at=timezone.now())
        self.message_user(request, f'{count} posts were published.', messages.SUCCESS)

    @admin.action(description='Unpublish selected posts')
    def unpublish_posts(self, request, queryset):
        count = queryset.update(status='draft', published_at=None)
        self.message_user(request, f'{count} posts were unpublished.', messages.WARNING)

    @admin.action(description='Reset view counts')
    def reset_views(self, request, queryset):
        count = queryset.update(views=0)
        self.message_user(request, f'View counts reset for {count} posts.', messages.INFO)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for Comment model."""
    list_display = ['author_name', 'post', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    list_editable = ['approved']
    search_fields = ['author_name', 'author_email', 'content']
    ordering = ['-created_at']
    list_per_page = 25
    actions = ['approve_comments', 'unapprove_comments']

    @admin.action(description='Approve selected comments')
    def approve_comments(self, request, queryset):
        count = queryset.update(approved=True)
        self.message_user(request, f'{count} comments were approved.', messages.SUCCESS)

    @admin.action(description='Unapprove selected comments')
    def unapprove_comments(self, request, queryset):
        count = queryset.update(approved=False)
        self.message_user(request, f'{count} comments were unapproved.', messages.WARNING)
