"""
Day 8: HTTP Request Examples using Python's requests library

This file demonstrates how to make HTTP requests in Python.
You'll use these skills when building and testing APIs.

Prerequisites:
    pip install requests
"""

import requests
import json

# ============================================
# Example 1: GET Request - Fetching Data
# ============================================

def get_example():
    """
    GET requests are used to retrieve data from a server.
    The response contains the data you requested.
    """
    print("=" * 50)
    print("GET Request Example")
    print("=" * 50)
    
    # Make a GET request to a public API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Check the status code
    print(f"Status Code: {response.status_code}")
    print(f"Status OK: {response.ok}")  # True if status code < 400
    
    # Get response headers
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    
    # Get response body as JSON
    data = response.json()
    print(f"Post Title: {data['title']}")
    print()


# ============================================
# Example 2: GET Request with Query Parameters
# ============================================

def get_with_params():
    """
    Query parameters are used to filter or customize requests.
    They appear after ? in the URL: /posts?userId=1
    """
    print("=" * 50)
    print("GET Request with Query Parameters")
    print("=" * 50)
    
    # Method 1: Include params in URL
    response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
    
    # Method 2: Use params dictionary (preferred)
    params = {
        "userId": 1,
        "_limit": 3  # Limit to 3 results
    }
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params=params
    )
    
    print(f"URL with params: {response.url}")
    print(f"Number of posts: {len(response.json())}")
    
    for post in response.json():
        print(f"  - {post['title'][:40]}...")
    print()


# ============================================
# Example 3: POST Request - Creating Data
# ============================================

def post_example():
    """
    POST requests are used to create new resources.
    The request body contains the data for the new resource.
    """
    print("=" * 50)
    print("POST Request Example")
    print("=" * 50)
    
    # Data to send
    new_post = {
        "title": "My New Blog Post",
        "body": "This is the content of my post.",
        "userId": 1
    }
    
    # Make POST request with JSON body
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=new_post  # Automatically sets Content-Type and encodes JSON
    )
    
    print(f"Status Code: {response.status_code}")  # Should be 201 Created
    print(f"Created Post: {response.json()}")
    print()


# ============================================
# Example 4: PUT Request - Updating Data
# ============================================

def put_example():
    """
    PUT requests are used to update/replace existing resources.
    The entire resource is replaced with the new data.
    """
    print("=" * 50)
    print("PUT Request Example")
    print("=" * 50)
    
    # Updated data (complete replacement)
    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "This is the updated content.",
        "userId": 1
    }
    
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=updated_post
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Updated Post: {response.json()}")
    print()


# ============================================
# Example 5: PATCH Request - Partial Update
# ============================================

def patch_example():
    """
    PATCH requests are used for partial updates.
    Only the specified fields are updated.
    """
    print("=" * 50)
    print("PATCH Request Example")
    print("=" * 50)
    
    # Only update the title
    partial_update = {
        "title": "Only Title Changed"
    }
    
    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=partial_update
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Updated Post: {response.json()}")
    print()


# ============================================
# Example 6: DELETE Request - Removing Data
# ============================================

def delete_example():
    """
    DELETE requests are used to remove resources.
    Usually returns 200 or 204 (No Content) on success.
    """
    print("=" * 50)
    print("DELETE Request Example")
    print("=" * 50)
    
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    
    print(f"Status Code: {response.status_code}")
    print(f"Resource deleted successfully!")
    print()


# ============================================
# Example 7: Handling Errors
# ============================================

def error_handling_example():
    """
    Always handle potential errors in HTTP requests.
    """
    print("=" * 50)
    print("Error Handling Example")
    print("=" * 50)
    
    # Example 1: 404 Not Found
    response = requests.get("https://jsonplaceholder.typicode.com/posts/999999")
    
    if response.status_code == 404:
        print("Post not found!")
    
    # Example 2: Using raise_for_status()
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/invalid")
        response.raise_for_status()  # Raises exception for 4xx/5xx errors
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    
    # Example 3: Network errors
    try:
        response = requests.get("https://invalid-domain-12345.com", timeout=3)
    except requests.exceptions.ConnectionError:
        print("Connection failed!")
    except requests.exceptions.Timeout:
        print("Request timed out!")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    print()


# ============================================
# Example 8: Request Headers
# ============================================

def headers_example():
    """
    Custom headers are often needed for authentication
    and specifying content types.
    """
    print("=" * 50)
    print("Request Headers Example")
    print("=" * 50)
    
    # Custom headers
    headers = {
        "Authorization": "Bearer your-token-here",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "MyApp/1.0"
    }
    
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        headers=headers
    )
    
    print(f"Request sent with custom headers")
    print(f"Response headers: {dict(response.headers)}")
    print()


# ============================================
# Example 9: Sessions (Maintaining State)
# ============================================

def session_example():
    """
    Sessions persist cookies and headers across multiple requests.
    Useful for authenticated APIs.
    """
    print("=" * 50)
    print("Session Example")
    print("=" * 50)
    
    # Create a session
    session = requests.Session()
    
    # Set default headers for all requests in this session
    session.headers.update({
        "Authorization": "Bearer my-token",
        "User-Agent": "MyApp/1.0"
    })
    
    # All requests through this session will include these headers
    response1 = session.get("https://jsonplaceholder.typicode.com/posts/1")
    response2 = session.get("https://jsonplaceholder.typicode.com/posts/2")
    
    print(f"Both requests used session headers")
    print(f"Post 1 title: {response1.json()['title'][:30]}...")
    print(f"Post 2 title: {response2.json()['title'][:30]}...")
    
    # Close the session when done
    session.close()
    print()


# ============================================
# Example 10: Downloading Content
# ============================================

def download_example():
    """
    Example of downloading binary content.
    """
    print("=" * 50)
    print("Download Example")
    print("=" * 50)
    
    # Download an image
    url = "https://via.placeholder.com/150"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Content-Length: {len(response.content)} bytes")
        
        # Save to file
        with open("/tmp/downloaded_image.png", "wb") as f:
            f.write(response.content)
        print("Image saved to /tmp/downloaded_image.png")
    
    print()


# ============================================
# Run All Examples
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("HTTP REQUEST EXAMPLES")
    print("=" * 50 + "\n")
    
    get_example()
    get_with_params()
    post_example()
    put_example()
    patch_example()
    delete_example()
    error_handling_example()
    headers_example()
    session_example()
    download_example()
    
    print("All examples completed!")
