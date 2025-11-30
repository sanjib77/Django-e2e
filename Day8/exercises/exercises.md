# Day 8: Practice Exercises

Complete these exercises to reinforce your understanding of web fundamentals.

---

## Exercise 1: HTTP Methods

Match each scenario with the correct HTTP method:

| Scenario | HTTP Method |
|----------|-------------|
| A) Fetching a user's profile | _____ |
| B) Creating a new blog post | _____ |
| C) Updating a user's entire profile | _____ |
| D) Removing a comment | _____ |
| E) Searching for products | _____ |
| F) Updating only the user's email | _____ |

Options: GET, POST, PUT, DELETE, PATCH

---

## Exercise 2: Status Codes

What status code would you expect in each scenario?

1. Successfully retrieved a list of users: _____
2. Created a new user account: _____
3. Tried to access a page that doesn't exist: _____
4. Submitted a form with invalid data: _____
5. Server crashed while processing request: _____
6. Not logged in but tried to access protected resource: _____
7. Logged in but don't have permission for the action: _____
8. Successfully deleted a resource (no content returned): _____

---

## Exercise 3: REST API Design

Design RESTful endpoints for a **Book Management System**:

Requirements:
- List all books
- Get a specific book
- Create a new book
- Update a book
- Delete a book
- Get all reviews for a book
- Add a review to a book

Write your endpoint design below:

```
# Books
GET    /________________    # List all books
GET    /________________    # Get book with ID 5
POST   /________________    # Create new book
PUT    /________________    # Update book with ID 5
DELETE /________________    # Delete book with ID 5

# Reviews
GET    /________________    # Get all reviews for book 5
POST   /________________    # Add review to book 5
```

---

## Exercise 4: JSON Practice

### 4a) Convert this Python dictionary to JSON:

```python
user = {
    "name": "Alice",
    "age": 28,
    "is_admin": False,
    "skills": ["Python", "Django", "JavaScript"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
```

Write the JSON output:
```json
{
    // Your answer here
}
```

### 4b) Given this JSON, write Python code to:

```json
{
    "products": [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 29.99},
        {"id": 3, "name": "Keyboard", "price": 79.99}
    ],
    "total_count": 3
}
```

1. Get the name of the second product
2. Get the price of the Keyboard
3. Calculate the total price of all products

```python
import json

json_string = '''... (the JSON above) ...'''

# Your code here:
data = json.loads(json_string)

# 1. Get name of second product
second_product_name = _______________

# 2. Get price of Keyboard
keyboard_price = _______________

# 3. Calculate total price
total_price = _______________
```

---

## Exercise 5: HTML Form Creation

Create an HTML form for a **Contact Us** page with the following fields:

- Name (text, required)
- Email (email, required)
- Subject (dropdown with options: General, Support, Sales, Partnership)
- Message (textarea, required)
- Subscribe to newsletter (checkbox)
- Submit button

```html
<!-- Write your HTML form here -->
<form method="POST" action="/contact">
    
    
    
</form>
```

---

## Exercise 6: Reading HTTP Requests

Given this HTTP request, answer the questions:

```
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer abc123token

{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secure123"
}
```

Questions:
1. What HTTP method is being used? _____
2. What is the endpoint being accessed? _____
3. What is the content type? _____
4. What type of authentication is being used? _____
5. What is being created? _____

---

## Exercise 7: Error Handling

Write Python code to make an HTTP request and handle potential errors:

```python
import requests

def safe_api_call(url):
    """
    Make a GET request to the URL and handle errors gracefully.
    Return the JSON data if successful, None if failed.
    """
    try:
        # Your code here:
        # 1. Make the GET request
        # 2. Check if status code indicates success
        # 3. Return JSON data
        # Handle exceptions for:
        # - Connection errors
        # - Timeout errors
        # - Invalid JSON response
        pass
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test with these URLs:
# safe_api_call("https://jsonplaceholder.typicode.com/posts/1")  # Should work
# safe_api_call("https://invalid-domain-xyz.com")  # Should handle error
# safe_api_call("https://jsonplaceholder.typicode.com/posts/99999")  # 404
```

---

## Exercise 8: API Response Analysis

Given this API response, answer the questions:

```json
{
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "Alice",
                "role": "admin",
                "posts_count": 15
            },
            {
                "id": 2,
                "name": "Bob",
                "role": "user",
                "posts_count": 8
            },
            {
                "id": 3,
                "name": "Charlie",
                "role": "user",
                "posts_count": 23
            }
        ],
        "pagination": {
            "page": 1,
            "per_page": 10,
            "total": 3,
            "total_pages": 1
        }
    },
    "errors": null
}
```

Questions:
1. How many users are in this response? _____
2. What is Charlie's role? _____
3. Which user has the most posts? _____
4. Is this the last page of results? _____ (yes/no)
5. Write Python code to get the total number of posts across all users:

```python
# Your code here:
total_posts = _____
```

---

## Exercise 9: URL Query Parameters

Given base URL: `https://api.example.com/products`

Write the full URLs for these requests:

1. Get products in the "electronics" category:
   URL: _____

2. Get products sorted by price in descending order:
   URL: _____

3. Get page 2 with 20 items per page:
   URL: _____

4. Search for products with "laptop" in the name, under $1000:
   URL: _____

5. Filter by multiple categories (electronics AND computers):
   URL: _____

---

## Exercise 10: Build a Mini API Spec

Design a complete API specification for a **Task Management System**:

### Requirements:
- Users can create, read, update, delete tasks
- Tasks have: id, title, description, status (pending/completed), due_date, user_id
- Users can mark tasks as complete
- Users can get all their tasks
- Users can filter tasks by status

### Your API Design:

```
# Endpoints:

# Tasks
GET    /api/_______              # List all tasks for current user
GET    /api/_______              # Get specific task
POST   /api/_______              # Create new task
PUT    /api/_______              # Update task
DELETE /api/_______              # Delete task
PATCH  /api/_______              # Mark task as complete

# Filtering
GET    /api/_______?_______      # Get only pending tasks
GET    /api/_______?_______      # Get only completed tasks

# Request body for creating a task:
{
    "_______": "_______",
    "_______": "_______",
    "_______": "_______"
}

# Response for getting a task:
{
    "_______": _______,
    "_______": "_______",
    "_______": "_______",
    "_______": "_______",
    "_______": "_______",
    "_______": _______
}
```

---

## Bonus Challenge: Mini Project

Build a simple Python script that:

1. Fetches data from a public API (e.g., jsonplaceholder.typicode.com)
2. Processes the JSON response
3. Displays formatted output
4. Handles errors gracefully

Example APIs to use:
- `https://jsonplaceholder.typicode.com/posts`
- `https://jsonplaceholder.typicode.com/users`
- `https://api.github.com/users/{username}`

```python
# Create your script in a new file called exercise_project.py
```

---

## Submission Guidelines

1. Complete all exercises in a text file or Python file
2. Test your code examples to make sure they work
3. Review your answers against the solutions
4. Make sure you understand any mistakes before moving on

---

**Good luck! Remember: Practice makes perfect! 🚀**
