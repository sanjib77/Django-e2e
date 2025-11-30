# Week 2 Assessment - Answer Key

## Section A: MCQs/True-False (6 points)

### Question 1
**Answer: C) 200**

Explanation: HTTP status code 200 means "OK" - the request was successful. 404 means "Not Found", 500 means "Internal Server Error", and 302 means "Found" (redirect).

---

### Question 2
**Answer: A) True**

Explanation: The `@login_required` decorator in Django checks if the user is authenticated. If not, it redirects them to the login URL specified in settings (LOGIN_URL).

---

### Question 3
**Answer: B) `git commit`**

Explanation: `git commit` saves changes to the local repository. `git add` stages changes, `git push` uploads to remote, and `git save` doesn't exist.

---

### Question 4
**Answer: C) WHERE**

Explanation: The `WHERE` clause filters rows based on specified conditions. `ORDER BY` sorts, `GROUP BY` groups, and `HAVING` filters groups.

---

### Question 5
**Answer: B) False**

Explanation: In Django's MTV (Model-Template-View) pattern, the **Template** is responsible for rendering HTML. The **View** contains business logic and handles requests/responses. This is different from traditional MVC where the View handles presentation.

---

### Question 6
**Answer: C) `Model.objects.all()`**

Explanation: `all()` returns a QuerySet of all objects. `get()` returns a single object, `filter()` returns filtered results, and `select()` doesn't exist in Django ORM.

---

## Section B: Short Coding Challenges (6 points)

### Question 7 (2 points)

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
```

**Grading:**
- 1 point: Correct field types (CharField, DecimalField, DateTimeField)
- 1 point: Correct parameters (max_length, max_digits, decimal_places, auto_now_add)

---

### Question 8 (2 points)

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
```

**Grading:**
- 1 point: Correct use of `render()` function with request and template
- 1 point: Correct QuerySet retrieval and context passing

---

### Question 9 (2 points)

```sql
SELECT * FROM users WHERE age > 18 ORDER BY name ASC;
```

**Grading:**
- 1 point: Correct SELECT and WHERE clause
- 1 point: Correct ORDER BY clause

---

## Section C: Conceptual Question (2 points)

### Question 10

**Model Answer:**

**GET Method:**
- Used to retrieve/read data from the server
- Data is sent in the URL as query parameters
- Should be idempotent (same request = same result)
- Can be bookmarked and cached
- Use cases: Viewing a webpage, searching, filtering data

**POST Method:**
- Used to submit/send data to the server
- Data is sent in the request body (not visible in URL)
- Not idempotent (may create new resources each time)
- Cannot be bookmarked
- Use cases: Creating new records, form submissions, login/authentication

**Grading:**
- 1 point: Correctly explains the difference (data retrieval vs submission)
- 1 point: Provides appropriate use cases for each

---

## 📊 Score Calculation

| Section | Your Score | Max Score |
|---------|------------|-----------|
| Section A (MCQs) | __ | 6 |
| Section B (Coding) | __ | 6 |
| Section C (Conceptual) | __ | 2 |
| **Total** | __ | **14** |

### Results:
- **10-14 points (70-100%)**: ✅ PASS - Ready for Week 3!
- **7-9 points (50-69%)**: ⚠️ Review needed - Study weak areas
- **0-6 points (0-49%)**: ❌ Retake - Review Week 2 material

---

**Congratulations on completing the Week 2 Assessment!** 🎉

If you passed, you're ready to move on to Week 3: APIs & Modern Web Dev!
