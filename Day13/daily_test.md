# Day 13: Daily Assessment
## Django Forms & Authentication Test

**Time Limit:** 15 minutes  
**Total Points:** 14  
**Passing Score:** 10 points (70%)

---

## Part A: Multiple Choice Questions (6 points)
*1 point each - Choose the best answer*

### Question 1
What method do you use to validate a specific field in a Django form?

A) `validate_<fieldname>()`  
B) `clean_<fieldname>()`  
C) `check_<fieldname>()`  
D) `filter_<fieldname>()`

---

### Question 2
Which Django decorator is used to restrict view access to logged-in users only?

A) `@auth_required`  
B) `@user_required`  
C) `@login_required`  
D) `@authenticated`

---

### Question 3
What template tag MUST be included inside a Django form to prevent CSRF attacks?

A) `{% csrf_protect %}`  
B) `{% csrf_token %}`  
C) `{% form_secure %}`  
D) `{% security_token %}`

---

### Question 4
True or False: `form.is_valid()` must be called before accessing `form.cleaned_data`.

A) True  
B) False

---

### Question 5
Which attribute in a ModelForm's Meta class specifies which model fields to include?

A) `include`  
B) `model_fields`  
C) `fields`  
D) `form_fields`

---

### Question 6
What function is used to log a user in programmatically after registration?

A) `authenticate(request, user)`  
B) `login(request, user)`  
C) `user.login(request)`  
D) `request.login(user)`

---

## Part B: Coding Challenges (6 points)
*2 points each*

### Question 7
Complete the Django form with custom validation to ensure the password is at least 8 characters:

```python
from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    
    # TODO: Add clean method to validate password length >= 8
```

---

### Question 8
Write a view function that:
1. Uses the `@login_required` decorator
2. Creates a new Post with the current user as author
3. Redirects to 'home' after successful creation

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# TODO: Complete the view function
```

---

### Question 9
Complete the template code to show different navigation options for logged-in vs anonymous users:

```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    
    <!-- TODO: Add conditional logic -->
    <!-- Show "Logout" and username if authenticated -->
    <!-- Show "Login" and "Register" if not authenticated -->
    
</nav>
```

---

## Part C: Conceptual Question (2 points)

### Question 10
Explain the difference between `clean()` and `clean_<fieldname>()` methods in Django forms. When would you use each?

---

# Answer Key

## Part A: Multiple Choice

1. **B) `clean_<fieldname>()`** - Django uses clean_ prefix for field-specific validation
2. **C) `@login_required`** - This is the standard decorator from django.contrib.auth.decorators
3. **B) `{% csrf_token %}`** - Required in all POST forms to prevent Cross-Site Request Forgery
4. **A) True** - cleaned_data is only populated after is_valid() returns True
5. **C) `fields`** - The fields attribute specifies which model fields to include
6. **B) `login(request, user)`** - This function from django.contrib.auth logs the user in

## Part B: Coding Challenges

### Question 7 Answer:
```python
from django import forms

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        return password
```

### Question 8 Answer:
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
```

### Question 9 Answer:
```html
<nav>
    <a href="{% url 'home' %}">Home</a>
    
    {% if user.is_authenticated %}
        <a href="{% url 'logout' %}">Logout ({{ user.username }})</a>
    {% else %}
        <a href="{% url 'login' %}">Login</a>
        <a href="{% url 'register' %}">Register</a>
    {% endif %}
</nav>
```

## Part C: Conceptual Question

### Question 10 Answer:
**`clean_<fieldname>()`** is used for validating a single specific field. It's called automatically during form validation and is ideal for field-specific rules like checking if an email is already registered or if a username contains invalid characters.

**`clean()`** is used for cross-field validation where you need to validate multiple fields together. It's called after all individual field clean methods. Use it when validation depends on the relationship between fields, such as checking if password and confirm_password match, or if end_date is after start_date.

---

## Scoring Guide

| Section | Points |
|---------|--------|
| Part A (Q1-Q6) | 6 points |
| Part B (Q7-Q9) | 6 points |
| Part C (Q10) | 2 points |
| **Total** | **14 points** |

**Pass:** 10+ points (70%)  
**Excellent:** 13+ points (93%)

---

## If You Scored Below 70%

Review these topics:
- Django Forms documentation
- Form validation methods
- `@login_required` decorator
- Template conditional logic with `{% if %}`
- The clean() vs clean_<fieldname>() distinction

Then retake the test tomorrow morning before proceeding to Day 14.
