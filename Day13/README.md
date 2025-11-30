# Day 13: Django Part 3 - Forms & Authentication

## 📅 Overview

Today we dive into Django's powerful form handling system and user authentication. By the end of this day, you'll be able to create and validate forms, implement complete user authentication (login, logout, register), and protect your views using decorators.

## 🎯 Learning Objectives

- Understand and create Django forms
- Implement form validation
- Build user authentication (login, logout, register)
- Protect views with `@login_required` decorator
- Apply these concepts in a practical blog project

---

## 📚 Topic 1: Django Forms

Django forms provide a powerful way to generate HTML forms, validate user input, and process submitted data.

### Creating a Basic Form

```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

### Using the Form in a View

```python
# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Do something with the data (e.g., send email, save to DB)
            return redirect('success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
```

### Rendering the Form in a Template

```html
<!-- templates/contact.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

### ModelForms - Forms from Models

ModelForms automatically create form fields from your model:

```python
# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

---

## 📚 Topic 2: Form Validation

### Built-in Validation

Django provides built-in validators for common cases:

```python
from django import forms
from django.core.validators import MinLengthValidator

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        validators=[MinLengthValidator(3)]
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput)
```

### Custom Field Validation

Use `clean_<fieldname>` methods for custom validation:

```python
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain spaces")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@company.com'):
            raise forms.ValidationError("Please use your company email")
        return email
```

### Cross-field Validation

Use the `clean()` method to validate multiple fields together:

```python
class RegistrationForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
```

### Displaying Validation Errors in Templates

```html
<form method="post">
    {% csrf_token %}
    
    <!-- Display non-field errors -->
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {{ form.non_field_errors }}
        </div>
    {% endif %}
    
    <!-- Display field errors -->
    {% for field in form %}
        <div class="form-group">
            {{ field.label_tag }}
            {{ field }}
            {% if field.errors %}
                <div class="error">{{ field.errors }}</div>
            {% endif %}
        </div>
    {% endfor %}
    
    <button type="submit">Submit</button>
</form>
```

---

## 📚 Topic 3: User Authentication

Django provides a complete authentication system out of the box.

### Setting Up Authentication URLs

```python
# urls.py (project level)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]
```

This includes these URLs automatically:
- `/accounts/login/` - Login page
- `/accounts/logout/` - Logout
- `/accounts/password_change/` - Change password
- `/accounts/password_reset/` - Reset password

### Creating Login Template

```html
<!-- templates/registration/login.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    
    {% if form.errors %}
        <p class="error">Invalid username or password</p>
    {% endif %}
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    
    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
</body>
</html>
```

### Custom User Registration

```python
# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
```

### Registration View

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            messages.success(request, f'Account created successfully!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register.html', {'form': form})
```

### Registration Template

```html
<!-- templates/registration/register.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h2>Create Account</h2>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    
    <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
</body>
</html>
```

### Custom Login View

```python
# views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in!')
            # Redirect to 'next' parameter if exists
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home')
```

### Settings Configuration

```python
# settings.py
LOGIN_REDIRECT_URL = 'home'  # Where to redirect after login
LOGOUT_REDIRECT_URL = 'home'  # Where to redirect after logout
LOGIN_URL = 'login'  # URL name for login page
```

---

## 📚 Topic 4: Protecting Views with @login_required

### Basic Usage

```python
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def create_post(request):
    # Only authenticated users can create posts
    # Implementation here
    pass
```

### Custom Login URL

```python
@login_required(login_url='/custom/login/')
def protected_view(request):
    return render(request, 'protected.html')
```

### Class-Based Views Protection

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### Checking User in Templates

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Logout</a>
{% else %}
    <a href="{% url 'login' %}">Login</a>
    <a href="{% url 'register' %}">Register</a>
{% endif %}
```

### User Permissions

```python
from django.contrib.auth.decorators import permission_required

@permission_required('blog.add_post')
def add_post(request):
    # Only users with 'blog.add_post' permission can access
    pass

# In class-based views
from django.contrib.auth.mixins import PermissionRequiredMixin

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
```

---

## 🛠️ Quick Project: Add User Auth to Blog

Let's build a complete blog with user authentication!

### Project Structure

```
blog_project/
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── home.html
│   └── registration/
│       ├── login.html
│       └── register.html
└── manage.py
```

### Step 1: Create the Blog Model

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
```

### Step 2: Create Forms

```python
# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
```

### Step 3: Create Views

```python
# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import UserRegisterForm, PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def register(request):
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
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Only author can edit
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
    post = get_object_or_404(Post, pk=pk)
    
    # Only author can delete
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
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/profile.html', {'posts': user_posts})
```

### Step 4: Configure URLs

```python
# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('post/new/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),
]

# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
]
```

### Step 5: Create Templates

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Blog{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        nav { background: #333; padding: 10px; margin-bottom: 20px; }
        nav a { color: white; margin-right: 15px; text-decoration: none; }
        .messages { padding: 10px; margin: 10px 0; }
        .success { background: #d4edda; color: #155724; }
        .error { background: #f8d7da; color: #721c24; }
        .post { border: 1px solid #ddd; padding: 15px; margin: 10px 0; }
        .btn { padding: 8px 15px; background: #007bff; color: white; border: none; cursor: pointer; }
        .btn-danger { background: #dc3545; }
    </style>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        {% if user.is_authenticated %}
            <a href="{% url 'create_post' %}">New Post</a>
            <a href="{% url 'profile' %}">Profile</a>
            <a href="{% url 'logout' %}">Logout ({{ user.username }})</a>
        {% else %}
            <a href="{% url 'login' %}">Login</a>
            <a href="{% url 'register' %}">Register</a>
        {% endif %}
    </nav>
    
    {% if messages %}
        {% for message in messages %}
            <div class="messages {{ message.tags }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
    
    {% block content %}{% endblock %}
</body>
</html>

<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Blog Posts</h1>
    
    {% for post in posts %}
        <div class="post">
            <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>
            <p>By {{ post.author.username }} on {{ post.created_at|date:"M d, Y" }}</p>
            <p>{{ post.content|truncatewords:30 }}</p>
        </div>
    {% empty %}
        <p>No posts yet.</p>
    {% endfor %}
{% endblock %}

<!-- templates/registration/login.html -->
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
    <h2>Login</h2>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn">Login</button>
    </form>
    
    <p>Don't have an account? <a href="{% url 'register' %}">Register here</a></p>
{% endblock %}

<!-- templates/registration/register.html -->
{% extends 'base.html' %}

{% block title %}Register{% endblock %}

{% block content %}
    <h2>Create Account</h2>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn">Register</button>
    </form>
    
    <p>Already have an account? <a href="{% url 'login' %}">Login here</a></p>
{% endblock %}

<!-- templates/blog/post_form.html -->
{% extends 'base.html' %}

{% block title %}{% if form.instance.pk %}Edit{% else %}New{% endif %} Post{% endblock %}

{% block content %}
    <h2>{% if form.instance.pk %}Edit{% else %}Create{% endif %} Post</h2>
    
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn">Save</button>
    </form>
{% endblock %}

<!-- templates/blog/post_detail.html -->
{% extends 'base.html' %}

{% block title %}{{ post.title }}{% endblock %}

{% block content %}
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author.username }} on {{ post.created_at|date:"M d, Y H:i" }}</p>
    
    <div>{{ post.content|linebreaks }}</div>
    
    {% if user == post.author %}
        <a href="{% url 'edit_post' post.pk %}" class="btn">Edit</a>
        <a href="{% url 'delete_post' post.pk %}" class="btn btn-danger">Delete</a>
    {% endif %}
{% endblock %}

<!-- templates/blog/post_confirm_delete.html -->
{% extends 'base.html' %}

{% block title %}Delete Post{% endblock %}

{% block content %}
    <h2>Confirm Delete</h2>
    <p>Are you sure you want to delete "{{ post.title }}"?</p>
    
    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Delete</button>
        <a href="{% url 'post_detail' post.pk %}" class="btn">Cancel</a>
    </form>
{% endblock %}

<!-- templates/blog/profile.html -->
{% extends 'base.html' %}

{% block title %}My Profile{% endblock %}

{% block content %}
    <h1>My Profile</h1>
    <p>Username: {{ user.username }}</p>
    <p>Email: {{ user.email }}</p>
    
    <h2>My Posts</h2>
    {% for post in posts %}
        <div class="post">
            <h3><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h3>
            <p>{{ post.created_at|date:"M d, Y" }}</p>
        </div>
    {% empty %}
        <p>You haven't written any posts yet.</p>
    {% endfor %}
{% endblock %}
```

### Step 6: Settings Configuration

```python
# settings.py (add these settings)

# Authentication settings
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Templates directory
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        # ... rest of settings
    },
]
```

---

## 🧪 Practice Exercises

### Exercise 1: Add Comment Form
Create a form that allows logged-in users to comment on posts.

### Exercise 2: User Profile Update
Create a form to let users update their profile (email, password).

### Exercise 3: Custom Validator
Add a custom validator to ensure post titles are unique per author.

---

## 📝 Key Takeaways

1. **Django Forms** simplify HTML form creation and data validation
2. **ModelForms** automatically generate forms from your models
3. **Custom validation** uses `clean_<fieldname>` and `clean()` methods
4. **Django Auth** provides login, logout, and user management out of the box
5. **@login_required** decorator protects views from unauthenticated access
6. **LoginRequiredMixin** is used for class-based views
7. Always use **{% csrf_token %}** in forms for security
8. Check **user.is_authenticated** in templates to show/hide content

---

## 📚 Additional Resources

- [Django Forms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Authentication](https://docs.djangoproject.com/en/stable/topics/auth/)
- [User Authentication Tutorial](https://docs.djangoproject.com/en/stable/topics/auth/default/)

---

## ⏭️ What's Next?

Tomorrow (Day 14), we'll build a complete mini-project combining everything from Week 2 - a Simple Blog or To-Do Web App with CRUD operations, user authentication, and database integration!
