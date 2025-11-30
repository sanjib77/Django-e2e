# Day 8: Daily Assessment Test

## Web & HTTP Fundamentals

**Time Limit:** 15 minutes  
**Total Points:** 14 points  
**Passing Score:** 10 points (70%)

---

## Section A: Multiple Choice / True-False (6 points)

**1 point each - Circle or write the correct answer**

---

### Question 1 (1 point)
Which HTTP method should be used to retrieve data from a server?

A) POST  
B) GET  
C) PUT  
D) DELETE

**Your Answer:** _____

---

### Question 2 (1 point)
What does the status code 404 indicate?

A) Server error  
B) Unauthorized access  
C) Resource not found  
D) Request successful

**Your Answer:** _____

---

### Question 3 (1 point)
True or False: In JSON, keys must be enclosed in double quotes.

**Your Answer:** _____

---

### Question 4 (1 point)
Which status code indicates that a new resource was successfully created?

A) 200  
B) 201  
C) 204  
D) 301

**Your Answer:** _____

---

### Question 5 (1 point)
In the client-server model, which component sends requests?

A) Server  
B) Database  
C) Client  
D) API

**Your Answer:** _____

---

### Question 6 (1 point)
True or False: PUT requests are used for partial updates to a resource. (Hint: Consider the difference between PUT and PATCH)

**Your Answer:** _____

---

## Section B: Short Coding Challenges (6 points)

**2 points each - Write the code or answer**

---

### Question 7 (2 points)
Write the correct Python code to convert this dictionary to a JSON string:

```python
data = {"name": "John", "age": 30}
```

**Your Answer:**
```python
import json

json_string = ________________________________
```

---

### Question 8 (2 points)
Design RESTful endpoints for a "Products" resource. Fill in the blanks:

```
GET    /_______________    # List all products
POST   /_______________    # Create a new product
GET    /_______________    # Get product with ID 5
DELETE /_______________    # Delete product with ID 5
```

---

### Question 9 (2 points)
Given this JSON response, write Python code to get the user's email:

```json
{
    "user": {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    },
    "success": true
}
```

```python
import json
response = '... (the JSON above) ...'
data = json.loads(response)

email = ________________________________
```

---

## Section C: Conceptual Question (2 points)

---

### Question 10 (2 points)
Explain the difference between HTTP status codes in the 4xx range versus the 5xx range. Give one example of each.

**Your Answer:**

4xx errors: ____________________________________________________________

____________________________________________________________

Example: ____________________________________________________________

5xx errors: ____________________________________________________________

____________________________________________________________

Example: ____________________________________________________________

---

## Answer Sheet

| Question | Your Answer | Points |
|----------|-------------|--------|
| 1 | | /1 |
| 2 | | /1 |
| 3 | | /1 |
| 4 | | /1 |
| 5 | | /1 |
| 6 | | /1 |
| 7 | | /2 |
| 8 | | /2 |
| 9 | | /2 |
| 10 | | /2 |
| **Total** | | **/14** |

---

## Scoring Guide

- **12-14 points**: Excellent! Ready for Day 9.
- **10-11 points**: Good job! You passed. Review any mistakes.
- **7-9 points**: Almost there. Review the material and retake tomorrow.
- **Below 7 points**: Need more practice. Review Day 8 thoroughly.

---

# Answer Key (For Self-Grading)

⚠️ **Grade yourself honestly! Only look after completing the test.**

<details>
<summary>Click to reveal answers</summary>

### Section A Answers:

1. **B) GET** - GET is used to retrieve/read data
2. **C) Resource not found** - 404 means the requested resource doesn't exist
3. **True** - JSON requires double quotes for keys: `{"key": "value"}`
4. **B) 201** - 201 Created indicates successful resource creation
5. **C) Client** - The client (browser, app) initiates requests
6. **False** - PUT is for complete replacement; PATCH is for partial updates

### Section B Answers:

7. **json_string = json.dumps(data)**
   - `json.dumps()` converts Python object to JSON string
   - `json.loads()` does the opposite (JSON string to Python)

8. RESTful endpoints:
   ```
   GET    /products      # List all products
   POST   /products      # Create a new product
   GET    /products/5    # Get product with ID 5
   DELETE /products/5    # Delete product with ID 5
   ```
   Also acceptable: `/api/products`, `/api/products/5`

9. **email = data["user"]["email"]**
   - Or: `email = data.get("user", {}).get("email")`
   - Result: `"alice@example.com"`

### Section C Answer:

10. **4xx vs 5xx errors:**

   **4xx (Client Errors):**
   - Indicate a problem with the request from the client
   - The client made an error (bad syntax, unauthorized, etc.)
   - Example: 404 Not Found, 401 Unauthorized, 400 Bad Request

   **5xx (Server Errors):**
   - Indicate a problem on the server side
   - The server failed to process a valid request
   - Example: 500 Internal Server Error, 503 Service Unavailable

   **Grading:** 
   - 1 point for correctly explaining the difference
   - 1 point for providing valid examples

</details>

---

**Good luck! 🍀**
