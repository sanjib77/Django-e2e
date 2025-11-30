# Day 8: Exercise Solutions

⚠️ **Try completing the exercises first before looking at these solutions!**

---

## Exercise 1: HTTP Methods - Solutions

| Scenario | HTTP Method |
|----------|-------------|
| A) Fetching a user's profile | **GET** |
| B) Creating a new blog post | **POST** |
| C) Updating a user's entire profile | **PUT** |
| D) Removing a comment | **DELETE** |
| E) Searching for products | **GET** |
| F) Updating only the user's email | **PATCH** |

---

## Exercise 2: Status Codes - Solutions

1. Successfully retrieved a list of users: **200 OK**
2. Created a new user account: **201 Created**
3. Tried to access a page that doesn't exist: **404 Not Found**
4. Submitted a form with invalid data: **400 Bad Request** (or 422 Unprocessable Entity)
5. Server crashed while processing request: **500 Internal Server Error**
6. Not logged in but tried to access protected resource: **401 Unauthorized**
7. Logged in but don't have permission for the action: **403 Forbidden**
8. Successfully deleted a resource (no content returned): **204 No Content**

---

## Exercise 3: REST API Design - Solutions

```
# Books
GET    /api/books           # List all books
GET    /api/books/5         # Get book with ID 5
POST   /api/books           # Create new book
PUT    /api/books/5         # Update book with ID 5
DELETE /api/books/5         # Delete book with ID 5

# Reviews
GET    /api/books/5/reviews     # Get all reviews for book 5
POST   /api/books/5/reviews     # Add review to book 5
```

---

## Exercise 4: JSON Practice - Solutions

### 4a) Python dict to JSON:

```json
{
    "name": "Alice",
    "age": 28,
    "is_admin": false,
    "skills": ["Python", "Django", "JavaScript"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
```

Note: `False` in Python becomes `false` in JSON (lowercase).

### 4b) JSON manipulation:

```python
import json

json_string = '''
{
    "products": [
        {"id": 1, "name": "Laptop", "price": 999.99},
        {"id": 2, "name": "Mouse", "price": 29.99},
        {"id": 3, "name": "Keyboard", "price": 79.99}
    ],
    "total_count": 3
}
'''

data = json.loads(json_string)

# 1. Get name of second product (index 1)
second_product_name = data["products"][1]["name"]  # "Mouse"

# 2. Get price of Keyboard
keyboard_price = data["products"][2]["price"]  # 79.99
# Or more robustly:
keyboard_price = next(p["price"] for p in data["products"] if p["name"] == "Keyboard")

# 3. Calculate total price
total_price = sum(product["price"] for product in data["products"])  # 1109.97
```

---

## Exercise 5: HTML Form Creation - Solution

```html
<form method="POST" action="/contact">
    <!-- Name Field -->
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
    </div>
    
    <!-- Email Field -->
    <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <!-- Subject Dropdown -->
    <div class="form-group">
        <label for="subject">Subject:</label>
        <select id="subject" name="subject">
            <option value="general">General</option>
            <option value="support">Support</option>
            <option value="sales">Sales</option>
            <option value="partnership">Partnership</option>
        </select>
    </div>
    
    <!-- Message Textarea -->
    <div class="form-group">
        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>
    </div>
    
    <!-- Newsletter Checkbox -->
    <div class="form-group">
        <label>
            <input type="checkbox" name="newsletter" value="yes">
            Subscribe to newsletter
        </label>
    </div>
    
    <!-- Submit Button -->
    <button type="submit">Send Message</button>
</form>
```

---

## Exercise 6: Reading HTTP Requests - Solutions

1. What HTTP method is being used? **POST**
2. What is the endpoint being accessed? **/api/users**
3. What is the content type? **application/json**
4. What type of authentication is being used? **Bearer Token (JWT)**
5. What is being created? **A new user account**

---

## Exercise 7: Error Handling - Solution

```python
import requests

def safe_api_call(url, timeout=10):
    """
    Make a GET request to the URL and handle errors gracefully.
    Return the JSON data if successful, None if failed.
    """
    try:
        # Make the GET request
        response = requests.get(url, timeout=timeout)
        
        # Check if status code indicates success (2xx)
        if response.ok:
            return response.json()
        elif response.status_code == 404:
            print(f"Resource not found: {url}")
            return None
        else:
            print(f"Error {response.status_code}: {response.reason}")
            return None
            
    except requests.exceptions.ConnectionError:
        print(f"Connection error: Could not connect to {url}")
        return None
    except requests.exceptions.Timeout:
        print(f"Timeout error: Request to {url} timed out")
        return None
    except requests.exceptions.JSONDecodeError:
        print(f"JSON error: Response is not valid JSON")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


# Test examples:
if __name__ == "__main__":
    # Should work
    result = safe_api_call("https://jsonplaceholder.typicode.com/posts/1")
    if result:
        print(f"Success! Got post: {result['title'][:30]}...")
    
    # Should handle 404
    result = safe_api_call("https://jsonplaceholder.typicode.com/posts/99999")
    
    # Should handle connection error
    result = safe_api_call("https://invalid-domain-xyz.com")
```

---

## Exercise 8: API Response Analysis - Solutions

1. How many users are in this response? **3**
2. What is Charlie's role? **user**
3. Which user has the most posts? **Charlie (23 posts)**
4. Is this the last page of results? **yes** (page 1 of 1)
5. Total posts calculation:

```python
data = {
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "role": "admin", "posts_count": 15},
            {"id": 2, "name": "Bob", "role": "user", "posts_count": 8},
            {"id": 3, "name": "Charlie", "role": "user", "posts_count": 23}
        ],
        "pagination": {
            "page": 1,
            "per_page": 10,
            "total": 3,
            "total_pages": 1
        }
    },
    "errors": None
}

total_posts = sum(user["posts_count"] for user in data["data"]["users"])
# total_posts = 46
```

---

## Exercise 9: URL Query Parameters - Solutions

Base URL: `https://api.example.com/products`

1. Get products in the "electronics" category:
   `https://api.example.com/products?category=electronics`

2. Get products sorted by price in descending order:
   `https://api.example.com/products?sort=price&order=desc`

3. Get page 2 with 20 items per page:
   `https://api.example.com/products?page=2&per_page=20`

4. Search for products with "laptop" in the name, under $1000:
   `https://api.example.com/products?search=laptop&max_price=1000`

5. Filter by multiple categories:
   `https://api.example.com/products?category=electronics&category=computers`
   or
   `https://api.example.com/products?categories=electronics,computers`

---

## Exercise 10: Task Management API Spec - Solution

```
# Endpoints:

# Tasks
GET    /api/tasks              # List all tasks for current user
GET    /api/tasks/1            # Get specific task (ID 1)
POST   /api/tasks              # Create new task
PUT    /api/tasks/1            # Update task (ID 1)
DELETE /api/tasks/1            # Delete task (ID 1)
PATCH  /api/tasks/1/complete   # Mark task as complete

# Filtering
GET    /api/tasks?status=pending     # Get only pending tasks
GET    /api/tasks?status=completed   # Get only completed tasks

# Request body for creating a task:
{
    "title": "Complete project",
    "description": "Finish the Django project by Friday",
    "due_date": "2024-01-15"
}

# Response for getting a task:
{
    "id": 1,
    "title": "Complete project",
    "description": "Finish the Django project by Friday",
    "status": "pending",
    "due_date": "2024-01-15",
    "user_id": 42
}
```

---

## Bonus Challenge - Sample Solution

```python
"""
Bonus Exercise: API Data Fetcher and Analyzer
"""
import requests
import json

def fetch_and_analyze_posts():
    """Fetch posts from JSONPlaceholder and analyze them."""
    
    print("=" * 50)
    print("Post Analysis Tool")
    print("=" * 50)
    
    # Fetch posts
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            timeout=10
        )
        response.raise_for_status()
        posts = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    # Basic statistics
    print(f"\nTotal posts: {len(posts)}")
    
    # Posts per user
    user_posts = {}
    for post in posts:
        user_id = post["userId"]
        user_posts[user_id] = user_posts.get(user_id, 0) + 1
    
    print("\nPosts per user:")
    for user_id, count in sorted(user_posts.items()):
        print(f"  User {user_id}: {count} posts")
    
    # Find longest title
    longest_post = max(posts, key=lambda p: len(p["title"]))
    print(f"\nLongest title:")
    print(f"  '{longest_post['title']}'")
    print(f"  ({len(longest_post['title'])} characters)")
    
    # Sample post
    print("\nSample post:")
    sample = posts[0]
    print(json.dumps(sample, indent=2))

def fetch_user_info(username):
    """Fetch and display GitHub user information."""
    
    print(f"\n{'=' * 50}")
    print(f"GitHub User: {username}")
    print("=" * 50)
    
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=10
        )
        
        if response.status_code == 404:
            print(f"User '{username}' not found")
            return
        
        response.raise_for_status()
        user = response.json()
        
        print(f"\nName: {user.get('name', 'N/A')}")
        print(f"Bio: {user.get('bio', 'N/A')}")
        print(f"Location: {user.get('location', 'N/A')}")
        print(f"Public Repos: {user.get('public_repos', 0)}")
        print(f"Followers: {user.get('followers', 0)}")
        print(f"Following: {user.get('following', 0)}")
        print(f"Profile: {user.get('html_url', 'N/A')}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_analyze_posts()
    fetch_user_info("octocat")  # GitHub's mascot account
```

---

## How Did You Do?

- **8-10 exercises correct**: Excellent! You're ready for Day 9!
- **6-7 exercises correct**: Good job! Review the ones you missed.
- **Below 6**: Review the lesson material and try again.

Remember: Understanding these fundamentals is crucial for Django development! 🚀
