from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import UserRegisterForm, PostForm


def home(request):
    """Display all blog posts."""
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def create_post(request):
    """Create a new blog post. Requires authentication."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def post_detail(request, pk):
    """Display a single blog post."""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def edit_post(request, pk):
    """Edit an existing blog post. Only author can edit."""
    post = get_object_or_404(Post, pk=pk)

    # Only author can edit their own posts
    if post.author != request.user:
        messages.error(request, 'You cannot edit this post')
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def delete_post(request, pk):
    """Delete a blog post. Only author can delete."""
    post = get_object_or_404(Post, pk=pk)

    # Only author can delete their own posts
    if post.author != request.user:
        messages.error(request, 'You cannot delete this post')
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def profile(request):
    """Display user profile with their posts."""
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/profile.html', {'posts': user_posts})
