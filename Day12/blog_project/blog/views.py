from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag


def post_list(request):
    """Display a list of all published posts."""
    posts_list = Post.objects.filter(status='published').select_related('author', 'category')
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts_list = posts_list.filter(category=category)
    
    # Filter by tag if provided
    tag_name = request.GET.get('tag')
    if tag_name:
        tag = get_object_or_404(Tag, name=tag_name)
        posts_list = posts_list.filter(tags=tag)
    
    # Pagination
    paginator = Paginator(posts_list, 10)  # 10 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    # Get all categories and tags for sidebar
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'current_category': category_slug,
        'current_tag': tag_name,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    """Display a single post."""
    post = get_object_or_404(
        Post.objects.select_related('author', 'category').prefetch_related('tags', 'comments'),
        slug=slug,
        status='published'
    )
    
    # Increment view count
    post.increment_views()
    
    # Get approved comments
    comments = post.comments.filter(approved=True)
    
    # Get related posts (same category)
    related_posts = Post.objects.filter(
        status='published',
        category=post.category
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)


def category_list(request):
    """Display all categories."""
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/category_list.html', context)


def tag_list(request):
    """Display all tags."""
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'blog/tag_list.html', context)
