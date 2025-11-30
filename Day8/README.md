# Day 8: Web & HTTP Fundamentals

Welcome to Day 8 of your intensive Python Web & AI/ML Developer bootcamp! Today we dive into the fundamentals of how the web works. Understanding these concepts is crucial before building web applications with Django.

## 📚 Today's Learning Objectives

By the end of today, you will:
- Understand the client-server architecture
- Know the main HTTP methods and when to use them
- Understand HTTP status codes and their meanings
- Grasp REST API fundamentals
- Work with JSON data format
- Know basic HTML for Django templates

---

## 1. How the Web Works (Client-Server Model)

### The Basic Concept

The web operates on a **client-server** model:

```
┌──────────────┐         Request          ┌──────────────┐
│              │ ────────────────────────▶ │              │
│    CLIENT    │                           │    SERVER    │
│  (Browser)   │ ◀──────────────────────── │  (Web App)   │
│              │         Response          │              │
└──────────────┘                           └──────────────┘
```

**Client**: The device/software requesting information (e.g., web browser, mobile app)

**Server**: The computer/software providing information (e.g., web server running Django)

### The Request-Response Cycle

1. **User Action**: User clicks a link or submits a form
2. **DNS Lookup**: Browser finds the server's IP address
3. **Request Sent**: Browser sends an HTTP request to the server
4. **Server Processing**: Server processes the request (runs your Django code)
5. **Response Sent**: Server sends back an HTTP response
6. **Rendering**: Browser displays the content to the user

### Example Flow

```python
# User visits: https://www.example.com/products/123

# 1. Client sends request:
#    GET /products/123 HTTP/1.1
#    Host: www.example.com

# 2. Server processes and returns:
#    HTTP/1.1 200 OK
#    Content-Type: text/html
#    
#    <html><body>Product Details...</body></html>
```

---

## 2. HTTP Methods (GET, POST, PUT, DELETE)

HTTP methods define **what action** you want to perform on a resource.

### The Four Main Methods

| Method | Purpose | Has Body | Idempotent | Safe |
|--------|---------|----------|------------|------|
| **GET** | Retrieve data | No | Yes | Yes |
| **POST** | Create new data | Yes | No | No |
| **PUT** | Update/Replace data | Yes | Yes | No |
| **DELETE** | Remove data | No | Yes | No |

### GET - Retrieve Data

```python
# Request to get user profile
# GET /users/42

# Use cases:
# - Loading a webpage
# - Fetching data from an API
# - Searching (with query parameters)

# Example with query parameters:
# GET /products?category=electronics&sort=price
```

### POST - Create Data

```python
# Request to create a new user
# POST /users
# Content-Type: application/json
# 
# {
#     "name": "John Doe",
#     "email": "john@example.com"
# }

# Use cases:
# - Submitting a registration form
# - Creating a new blog post
# - Uploading a file
```

### PUT - Update/Replace Data

```python
# Request to update user with ID 42
# PUT /users/42
# Content-Type: application/json
# 
# {
#     "name": "John Updated",
#     "email": "john.updated@example.com"
# }

# Use cases:
# - Updating user profile
# - Editing a blog post
# - Replacing configuration settings
```

### DELETE - Remove Data

```python
# Request to delete user with ID 42
# DELETE /users/42

# Use cases:
# - Deleting a user account
# - Removing a blog post
# - Canceling an order
```

### Additional Methods (Quick Overview)

- **PATCH**: Partial update (only specific fields)
- **HEAD**: Like GET but returns only headers
- **OPTIONS**: Returns allowed methods for a resource

---

## 3. HTTP Status Codes

Status codes tell the client what happened with their request.

### Categories

| Range | Category | Meaning |
|-------|----------|---------|
| **1xx** | Informational | Request received, continuing |
| **2xx** | Success | Request successfully processed |
| **3xx** | Redirection | Further action needed |
| **4xx** | Client Error | Problem with the request |
| **5xx** | Server Error | Server failed to process |

### Essential Status Codes to Know

#### Success (2xx)
```python
200 OK              # Request succeeded
201 Created         # New resource created (after POST)
204 No Content      # Success but no content to return (after DELETE)
```

#### Redirection (3xx)
```python
301 Moved Permanently   # Resource permanently moved
302 Found              # Temporary redirect
304 Not Modified       # Cached version is still valid
```

#### Client Errors (4xx)
```python
400 Bad Request         # Invalid request syntax
401 Unauthorized        # Authentication required
403 Forbidden           # Access denied (even with auth)
404 Not Found           # Resource doesn't exist
405 Method Not Allowed  # HTTP method not supported
422 Unprocessable Entity # Validation error
```

#### Server Errors (5xx)
```python
500 Internal Server Error   # Generic server error
502 Bad Gateway            # Invalid response from upstream
503 Service Unavailable    # Server temporarily overloaded
504 Gateway Timeout        # Upstream server timed out
```

### Real-World Examples

```python
# Login attempt
# - 200: Login successful
# - 401: Invalid credentials
# - 403: Account locked

# Create new post
# - 201: Post created successfully
# - 400: Missing required fields
# - 401: Not logged in
# - 500: Database error

# View product page
# - 200: Product found, displaying
# - 404: Product doesn't exist
```

---

## 4. REST API Basics

### What is REST?

**REST** (Representational State Transfer) is an architectural style for designing web APIs.

### REST Principles

1. **Stateless**: Each request contains all needed information
2. **Client-Server**: Separation of concerns
3. **Uniform Interface**: Consistent API structure
4. **Resource-Based**: Everything is a resource with a unique URL

### RESTful URL Design

```python
# Good RESTful URLs (noun-based, resource-oriented)
GET    /users           # List all users
GET    /users/42        # Get user with ID 42
POST   /users           # Create new user
PUT    /users/42        # Update user 42
DELETE /users/42        # Delete user 42

# Nested resources
GET    /users/42/posts         # Get all posts by user 42
GET    /users/42/posts/7       # Get post 7 by user 42
POST   /users/42/posts         # Create post for user 42

# Bad URLs (avoid these)
GET    /getUser?id=42          # Don't use verbs in URLs
POST   /createNewUser          # Don't describe actions in URLs
GET    /user/42/delete         # Don't put actions in URLs
```

### REST API Example

```python
# Blog API Design

# Posts
GET    /api/posts              # List all posts
GET    /api/posts/1            # Get post 1
POST   /api/posts              # Create new post
PUT    /api/posts/1            # Update post 1
DELETE /api/posts/1            # Delete post 1

# Comments on a post
GET    /api/posts/1/comments   # Get comments on post 1
POST   /api/posts/1/comments   # Add comment to post 1

# Query parameters for filtering/sorting
GET    /api/posts?author=john&sort=date
GET    /api/posts?page=2&limit=10
```

---

## 5. JSON Format

### What is JSON?

**JSON** (JavaScript Object Notation) is the standard format for data exchange in modern APIs.

### JSON Syntax Rules

- Data is in key/value pairs
- Keys must be strings in double quotes
- Data is separated by commas
- Objects are enclosed in curly braces `{}`
- Arrays are enclosed in square brackets `[]`

### JSON Data Types

```json
{
    "string": "Hello World",
    "number": 42,
    "float": 3.14,
    "boolean": true,
    "null": null,
    "array": [1, 2, 3],
    "object": {
        "nested": "value"
    }
}
```

### Real API Response Examples

```json
// Single user response
{
    "id": 42,
    "name": "John Doe",
    "email": "john@example.com",
    "is_active": true,
    "created_at": "2024-01-15T10:30:00Z"
}

// List of users response
{
    "count": 100,
    "next": "/api/users?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Alice"
        },
        {
            "id": 2,
            "name": "Bob"
        }
    ]
}

// Error response
{
    "error": true,
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": {
        "field": "email",
        "provided": "not-an-email"
    }
}
```

### Python and JSON

```python
import json

# Python dict to JSON string
user = {"name": "John", "age": 30}
json_string = json.dumps(user)
print(json_string)  # '{"name": "John", "age": 30}'

# JSON string to Python dict
json_data = '{"name": "Jane", "age": 25}'
python_dict = json.loads(json_data)
print(python_dict["name"])  # Jane

# Pretty print JSON
print(json.dumps(user, indent=2))
# {
#   "name": "John",
#   "age": 30
# }
```

---

## 6. HTML Basics (For Django Templates)

### Essential HTML Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

### Common HTML Elements

```html
<!-- Headings -->
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection</h3>

<!-- Paragraphs and Text -->
<p>This is a paragraph.</p>
<strong>Bold text</strong>
<em>Italic text</em>

<!-- Links -->
<a href="https://example.com">Click here</a>
<a href="/about">About page</a>

<!-- Images -->
<img src="photo.jpg" alt="Description of image">

<!-- Lists -->
<ul>
    <li>Unordered item 1</li>
    <li>Unordered item 2</li>
</ul>

<ol>
    <li>Ordered item 1</li>
    <li>Ordered item 2</li>
</ol>

<!-- Divs and Spans -->
<div class="container">Block-level container</div>
<span class="highlight">Inline element</span>
```

### HTML Forms (Critical for Web Apps)

```html
<form method="POST" action="/submit">
    <!-- Text Input -->
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    
    <!-- Email Input -->
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    
    <!-- Password Input -->
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
    
    <!-- Textarea -->
    <label for="bio">Bio:</label>
    <textarea id="bio" name="bio" rows="4"></textarea>
    
    <!-- Select Dropdown -->
    <label for="country">Country:</label>
    <select id="country" name="country">
        <option value="us">United States</option>
        <option value="uk">United Kingdom</option>
        <option value="ca">Canada</option>
    </select>
    
    <!-- Checkbox -->
    <input type="checkbox" id="terms" name="terms">
    <label for="terms">I agree to terms</label>
    
    <!-- Radio Buttons -->
    <input type="radio" name="gender" value="male"> Male
    <input type="radio" name="gender" value="female"> Female
    
    <!-- Submit Button -->
    <button type="submit">Submit</button>
</form>
```

### Tables

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>John Doe</td>
            <td>john@example.com</td>
            <td>Admin</td>
        </tr>
        <tr>
            <td>Jane Smith</td>
            <td>jane@example.com</td>
            <td>User</td>
        </tr>
    </tbody>
</table>
```

### Django Template Syntax Preview

```html
<!-- Variables -->
<h1>{{ page_title }}</h1>
<p>Hello, {{ user.name }}!</p>

<!-- Loops -->
<ul>
{% for item in items %}
    <li>{{ item.name }}</li>
{% endfor %}
</ul>

<!-- Conditionals -->
{% if user.is_authenticated %}
    <p>Welcome back!</p>
{% else %}
    <a href="/login">Please log in</a>
{% endif %}

<!-- Template Inheritance -->
{% extends "base.html" %}
{% block content %}
    <h1>Page Content</h1>
{% endblock %}
```

---

## 📝 Quick Reference Cheat Sheet

### HTTP Methods Summary
```
GET    - Read data (safe, no side effects)
POST   - Create new data
PUT    - Update/Replace data
DELETE - Remove data
PATCH  - Partial update
```

### Status Codes to Remember
```
200 - OK
201 - Created
204 - No Content
301 - Moved Permanently
400 - Bad Request
401 - Unauthorized
403 - Forbidden
404 - Not Found
500 - Internal Server Error
```

### JSON Format
```json
{
    "string": "value",
    "number": 42,
    "boolean": true,
    "null": null,
    "array": [],
    "object": {}
}
```

---

## 📂 Files in This Folder

- `README.md` - This lesson content
- `examples/` - Code examples
  - `http_request_example.py` - Making HTTP requests with Python
  - `json_example.py` - Working with JSON in Python
  - `html_example.html` - HTML template example
- `exercises/` - Practice exercises
  - `exercises.md` - Practice problems
  - `solutions.md` - Solutions (try first before looking!)
- `test/` - Daily assessment
  - `day8_test.md` - Today's test (10 questions, 14 points)

---

## 🎯 Today's Goals Checklist

- [ ] Understand client-server architecture
- [ ] Know when to use GET, POST, PUT, DELETE
- [ ] Memorize essential HTTP status codes
- [ ] Understand REST API design principles
- [ ] Be comfortable reading and writing JSON
- [ ] Know basic HTML elements for templates
- [ ] Complete practice exercises
- [ ] Pass daily assessment (70%+)

---

## 🔗 Next Steps

Tomorrow (Day 9), we'll learn **Git Version Control** - essential for every developer!

Keep practicing and see you tomorrow! 🚀
