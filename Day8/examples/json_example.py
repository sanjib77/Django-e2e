"""
Day 8: JSON Examples in Python

This file demonstrates working with JSON data in Python.
JSON is the standard format for API communication.
"""

import json
from datetime import datetime

# ============================================
# Example 1: Python to JSON (Serialization)
# ============================================

def python_to_json_example():
    """
    Converting Python objects to JSON strings.
    This is called 'serialization' or 'encoding'.
    """
    print("=" * 50)
    print("Python to JSON (Serialization)")
    print("=" * 50)
    
    # Python dictionary
    user = {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com",
        "is_active": True,
        "roles": ["admin", "user"],
        "profile": {
            "bio": "Software developer",
            "website": None
        }
    }
    
    # Convert to JSON string
    json_string = json.dumps(user)
    print(f"JSON string:\n{json_string}\n")
    
    # Pretty print with indentation
    json_pretty = json.dumps(user, indent=2)
    print(f"Pretty JSON:\n{json_pretty}\n")
    
    # Sorted keys
    json_sorted = json.dumps(user, indent=2, sort_keys=True)
    print(f"Sorted keys:\n{json_sorted}\n")


# ============================================
# Example 2: JSON to Python (Deserialization)
# ============================================

def json_to_python_example():
    """
    Converting JSON strings to Python objects.
    This is called 'deserialization' or 'decoding'.
    """
    print("=" * 50)
    print("JSON to Python (Deserialization)")
    print("=" * 50)
    
    # JSON string (like from an API response)
    json_string = '''
    {
        "id": 42,
        "title": "Hello World",
        "published": true,
        "views": 1500,
        "tags": ["python", "tutorial"],
        "author": {
            "name": "Jane Smith",
            "email": "jane@example.com"
        }
    }
    '''
    
    # Convert to Python dictionary
    data = json.loads(json_string)
    
    print(f"Type: {type(data)}")
    print(f"Title: {data['title']}")
    print(f"Author: {data['author']['name']}")
    print(f"Tags: {', '.join(data['tags'])}")
    print(f"Published: {data['published']}")
    print()


# ============================================
# Example 3: Reading JSON from File
# ============================================

def read_json_file_example():
    """
    Reading JSON data from a file.
    Common for configuration files.
    """
    print("=" * 50)
    print("Reading JSON from File")
    print("=" * 50)
    
    # Create a sample JSON file first
    sample_data = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp_db"
        },
        "debug": True,
        "allowed_hosts": ["localhost", "127.0.0.1"]
    }
    
    # Write to file
    with open("/tmp/config.json", "w") as f:
        json.dump(sample_data, f, indent=2)
    print("Created /tmp/config.json")
    
    # Read from file
    with open("/tmp/config.json", "r") as f:
        config = json.load(f)
    
    print(f"Database host: {config['database']['host']}")
    print(f"Debug mode: {config['debug']}")
    print(f"Allowed hosts: {config['allowed_hosts']}")
    print()


# ============================================
# Example 4: Writing JSON to File
# ============================================

def write_json_file_example():
    """
    Writing Python data to a JSON file.
    """
    print("=" * 50)
    print("Writing JSON to File")
    print("=" * 50)
    
    # Data to save
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ]
    
    # Write to file with pretty formatting
    with open("/tmp/users.json", "w") as f:
        json.dump(users, f, indent=2)
    
    print("Saved users to /tmp/users.json")
    
    # Verify by reading back
    with open("/tmp/users.json", "r") as f:
        loaded = json.load(f)
        print(f"Loaded {len(loaded)} users from file")
    print()


# ============================================
# Example 5: JSON Type Mapping
# ============================================

def type_mapping_example():
    """
    Understanding how Python types map to JSON types.
    """
    print("=" * 50)
    print("JSON Type Mapping")
    print("=" * 50)
    
    # Python to JSON type mapping
    python_data = {
        "string": "hello",           # str -> string
        "integer": 42,               # int -> number
        "float": 3.14,               # float -> number
        "boolean_true": True,        # True -> true
        "boolean_false": False,      # False -> false
        "none_value": None,          # None -> null
        "list": [1, 2, 3],           # list -> array
        "dict": {"key": "value"}     # dict -> object
    }
    
    json_str = json.dumps(python_data, indent=2)
    print(f"Python -> JSON:\n{json_str}\n")
    
    # Note: Some Python types are NOT JSON serializable
    # - datetime objects
    # - sets
    # - custom objects
    # - bytes
    print()


# ============================================
# Example 6: Handling Non-Serializable Types
# ============================================

def custom_encoder_example():
    """
    Handling Python types that are not JSON serializable.
    """
    print("=" * 50)
    print("Custom JSON Encoder")
    print("=" * 50)
    
    # This will fail by default:
    # data = {"timestamp": datetime.now()}
    # json.dumps(data)  # TypeError!
    
    # Solution 1: Convert before serializing
    data = {
        "name": "Event",
        "timestamp": datetime.now().isoformat()
    }
    print(f"With ISO format: {json.dumps(data)}\n")
    
    # Solution 2: Custom encoder
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, set):
                return list(obj)
            return super().default(obj)
    
    data_with_datetime = {
        "name": "Event",
        "timestamp": datetime.now(),
        "tags": {"python", "json", "tutorial"}
    }
    
    result = json.dumps(data_with_datetime, cls=CustomEncoder, indent=2)
    print(f"With custom encoder:\n{result}\n")


# ============================================
# Example 7: JSON Validation
# ============================================

def json_validation_example():
    """
    Validating JSON strings.
    """
    print("=" * 50)
    print("JSON Validation")
    print("=" * 50)
    
    valid_json = '{"name": "John", "age": 30}'
    invalid_json = "{'name': 'John', 'age': 30}"  # Single quotes are invalid
    
    def is_valid_json(json_string):
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return False
    
    print(f"Valid JSON test: {is_valid_json(valid_json)}")
    print(f"Invalid JSON test: {is_valid_json(invalid_json)}")
    print()


# ============================================
# Example 8: API Response Handling
# ============================================

def api_response_example():
    """
    Common patterns for handling API JSON responses.
    """
    print("=" * 50)
    print("API Response Handling")
    print("=" * 50)
    
    # Simulated API response
    api_response = '''
    {
        "success": true,
        "data": {
            "users": [
                {"id": 1, "name": "Alice", "role": "admin"},
                {"id": 2, "name": "Bob", "role": "user"},
                {"id": 3, "name": "Charlie", "role": "user"}
            ],
            "total": 3,
            "page": 1
        },
        "errors": []
    }
    '''
    
    response = json.loads(api_response)
    
    # Check success
    if response["success"]:
        users = response["data"]["users"]
        
        print(f"Total users: {response['data']['total']}")
        print("\nUser list:")
        for user in users:
            print(f"  - {user['name']} ({user['role']})")
    else:
        print(f"Errors: {response['errors']}")
    
    print()


# ============================================
# Example 9: Nested JSON Access
# ============================================

def nested_json_example():
    """
    Safely accessing nested JSON data.
    """
    print("=" * 50)
    print("Nested JSON Access")
    print("=" * 50)
    
    data = {
        "company": {
            "name": "Tech Corp",
            "departments": {
                "engineering": {
                    "employees": [
                        {"name": "Alice", "title": "Senior Dev"},
                        {"name": "Bob", "title": "Junior Dev"}
                    ]
                }
            }
        }
    }
    
    # Deep access
    first_engineer = data["company"]["departments"]["engineering"]["employees"][0]
    print(f"First engineer: {first_engineer['name']}")
    
    # Safe access with .get() to avoid KeyError
    marketing = data["company"]["departments"].get("marketing", {})
    marketing_employees = marketing.get("employees", [])
    print(f"Marketing employees: {marketing_employees}")
    
    # Using try/except for complex paths
    try:
        sales_lead = data["company"]["departments"]["sales"]["lead"]
    except KeyError:
        sales_lead = "Not found"
    print(f"Sales lead: {sales_lead}")
    
    print()


# ============================================
# Example 10: JSON in Practice - Config File
# ============================================

def config_file_example():
    """
    Real-world example: Application configuration.
    """
    print("=" * 50)
    print("Configuration File Example")
    print("=" * 50)
    
    # Django-like settings as JSON
    config = {
        "django": {
            "debug": True,
            "allowed_hosts": ["localhost", "127.0.0.1"],
            "secret_key": "your-secret-key-here"
        },
        "database": {
            "engine": "postgresql",
            "name": "myapp_db",
            "user": "postgres",
            "password": "password123",
            "host": "localhost",
            "port": 5432
        },
        "email": {
            "backend": "smtp",
            "host": "smtp.gmail.com",
            "port": 587,
            "use_tls": True
        },
        "logging": {
            "level": "INFO",
            "file": "/var/log/myapp.log"
        }
    }
    
    # Save config
    config_path = "/tmp/app_config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to {config_path}")
    
    # Load and use config
    with open(config_path, "r") as f:
        settings = json.load(f)
    
    print(f"\nApplication Settings:")
    print(f"  Debug: {settings['django']['debug']}")
    print(f"  Database: {settings['database']['engine']}://{settings['database']['host']}")
    print(f"  Email: {settings['email']['host']}")
    print()


# ============================================
# Run All Examples
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("JSON EXAMPLES IN PYTHON")
    print("=" * 50 + "\n")
    
    python_to_json_example()
    json_to_python_example()
    read_json_file_example()
    write_json_file_example()
    type_mapping_example()
    custom_encoder_example()
    json_validation_example()
    api_response_example()
    nested_json_example()
    config_file_example()
    
    print("All examples completed!")
