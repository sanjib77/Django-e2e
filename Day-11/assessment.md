# Day 11: Daily Assessment

## Django Part 1 - Setup & Basics

**Total Points: 14**  
**Time Limit: 15 minutes**  
**Passing Score: 70% (10 points)**

---

## Part A: Multiple Choice Questions (6 points)
*1 point each*

### Question 1
What command is used to create a new Django project?

- A) `python django startproject myproject`
- B) `django-admin startproject myproject`
- C) `pip install django myproject`
- D) `python manage.py startproject myproject`

---

### Question 2
Which file contains the main configuration settings for a Django project?

- A) `manage.py`
- B) `urls.py`
- C) `settings.py`
- D) `wsgi.py`

---

### Question 3
What is the correct command to create a new Django app named "blog"?

- A) `django-admin createapp blog`
- B) `python manage.py startapp blog`
- C) `django-admin startapp blog`
- D) `python manage.py createapp blog`

---

### Question 4
In Django's MTV architecture, what does the "V" stand for?

- A) Visual
- B) Variable
- C) View
- D) Virtual

---

### Question 5
Which Django template tag is used for template inheritance?

- A) `{% include %}`
- B) `{% extends %}`
- C) `{% inherit %}`
- D) `{% parent %}`

---

### Question 6
What is the default port number when running Django's development server?

- A) 80
- B) 3000
- C) 8000
- D) 5000

---

## Part B: Short Coding Challenges (6 points)
*2 points each*

### Challenge 1
Write a function-based view called `about` that renders a template named `about.html`.

```python
# Write your code here:



```

---

### Challenge 2
Write a URL pattern that:
1. Matches the path `/product/<id>/` where `id` is an integer
2. Calls a view function named `product_detail`
3. Has the name `product-detail`

```python
# Write your code here:



```

---

### Challenge 3
Write the correct Django template syntax to:
1. Display a variable called `username` in uppercase
2. Check if `items` list is not empty and display each item

```html
<!-- Write your code here: -->




```

---

## Part C: Concept Explanation (2 points)

### Question
Explain the difference between a Django **project** and a Django **app**. When would you create multiple apps within a single project?

```
Write your answer here:




```

---

## Answer Key

<details>
<summary>Click to reveal answers</summary>

### Part A: Multiple Choice

1. **B** - `django-admin startproject myproject`
2. **C** - `settings.py`
3. **B** - `python manage.py startapp blog`
4. **C** - View
5. **B** - `{% extends %}`
6. **C** - 8000

### Part B: Coding Challenges

**Challenge 1:**
```python
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')
```

**Challenge 2:**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>/', views.product_detail, name='product-detail'),
]
```

**Challenge 3:**
```html
<p>{{ username|upper }}</p>

{% if items %}
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
{% endif %}
```

### Part C: Concept Explanation

**Sample Answer:**
A Django **project** is the entire web application, containing settings, URL configurations, and overall structure. An **app** is a modular component within the project that handles specific functionality.

You would create multiple apps when:
- Building a large application with distinct features (e.g., users app, blog app, shop app)
- Creating reusable components that can be used in other projects
- Organizing code by functionality for better maintainability
- Working with teams where different developers work on different apps

</details>

---

## Scoring

| Section | Your Score | Max Score |
|---------|------------|-----------|
| Part A  |            | 6         |
| Part B  |            | 6         |
| Part C  |            | 2         |
| **Total** |          | **14**    |

**Result:** Pass (≥10 points) / Need Review (<10 points)

---

## Notes for Review

If you scored below 70%, review these topics:
- [ ] Django project and app creation commands
- [ ] File structure and purpose of each file
- [ ] URL routing syntax
- [ ] Function-based views
- [ ] Template syntax and tags
