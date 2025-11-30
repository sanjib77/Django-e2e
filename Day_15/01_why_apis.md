# Why APIs?

## 🤔 What is an API?

**API** stands for **Application Programming Interface**. Think of it as a waiter in a restaurant:
- You (the client) tell the waiter (API) what you want
- The waiter goes to the kitchen (server/database) 
- The waiter brings back your food (data)

You don't need to know HOW the kitchen works - you just need to know how to order!

## 🌐 Real-World Examples

| App | API Use |
|-----|---------|
| Weather App | Gets weather data from a weather service API |
| Uber | Uses Google Maps API for directions |
| Social Login | Uses Facebook/Google APIs for authentication |
| Payment | Uses Stripe/PayPal APIs to process payments |

## 📡 What is REST?

**REST** (Representational State Transfer) is a set of rules for building APIs. REST APIs use:

### HTTP Methods (CRUD Operations)

| Method | Purpose | Example |
|--------|---------|---------|
| `GET` | Read data | Get all users |
| `POST` | Create data | Create new user |
| `PUT` | Update data (full) | Update entire user profile |
| `PATCH` | Update data (partial) | Update just email |
| `DELETE` | Delete data | Delete a user |

### Standard URL Patterns

```
GET    /api/books/        → List all books
GET    /api/books/1/      → Get book with id=1
POST   /api/books/        → Create new book
PUT    /api/books/1/      → Update book with id=1
DELETE /api/books/1/      → Delete book with id=1
```

## 📦 JSON - The Language of APIs

APIs communicate using **JSON** (JavaScript Object Notation):

```json
{
    "id": 1,
    "title": "Django for Beginners",
    "author": "William Vincent",
    "price": 29.99,
    "in_stock": true,
    "categories": ["web development", "python"]
}
```

### Why JSON?
- ✅ Human-readable
- ✅ Lightweight
- ✅ Supported by all programming languages
- ✅ Easy to parse

## 🏗️ API Architecture

```
┌─────────────┐     HTTP Request      ┌─────────────┐
│   Client    │ ─────────────────────▶│    API      │
│ (Browser,   │                       │   Server    │
│  Mobile App,│◀───────────────────── │  (Django)   │
│  Other App) │     HTTP Response     │             │
└─────────────┘        (JSON)         └─────────────┘
                                            │
                                            ▼
                                      ┌─────────────┐
                                      │  Database   │
                                      └─────────────┘
```

## 🎯 Why Do We Need APIs?

### 1. **Separation of Concerns**
- Frontend (React, Vue, Mobile) can be developed separately from backend
- Same API can serve web, mobile, and third-party apps

### 2. **Scalability**
- API can be hosted on different servers
- Easier to scale individual components

### 3. **Reusability**
- One API, multiple clients
- Build once, use everywhere

### 4. **Third-Party Integration**
- Let other developers build on your platform
- Examples: Twitter API, GitHub API, Stripe API

## 📊 HTTP Status Codes

Your API should return appropriate status codes:

| Code | Meaning | Use Case |
|------|---------|----------|
| `200` | OK | Successful GET or PUT |
| `201` | Created | Successful POST |
| `204` | No Content | Successful DELETE |
| `400` | Bad Request | Invalid data sent |
| `401` | Unauthorized | Not logged in |
| `403` | Forbidden | No permission |
| `404` | Not Found | Resource doesn't exist |
| `500` | Server Error | Something broke |

## 💡 Quick Exercise

**Think about an API you use daily:**

1. What app uses it?
2. What data does it request/send?
3. What would break if the API stopped working?

Example Answer:
- App: Spotify
- Data: Song metadata, playlists, user preferences
- If broken: Can't play music, see playlists, or get recommendations

## 🔑 Key Points to Remember

1. **APIs enable communication** between different software systems
2. **REST** is a standard way to structure APIs
3. **HTTP methods** correspond to CRUD operations
4. **JSON** is the standard data format
5. **Status codes** tell clients what happened with their request

---

**Next:** [Installing DRF](./02_installing_drf.md)
