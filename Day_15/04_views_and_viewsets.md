# API Views and ViewSets

## 🎯 Overview

DRF provides several ways to build API views, from simple to powerful:

```
Function-based Views → APIView → Generic Views → ViewSets
    (Simplest)                                    (Most Powerful)
```

## 1️⃣ Function-Based Views (Simple)

Good for learning and simple endpoints:

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    """
    List all books or create a new book
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    Retrieve, update or delete a book
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### URL Configuration

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
]
```

## 2️⃣ Class-Based APIView

More organized, reusable, and Pythonic:

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookList(APIView):
    """
    List all books or create a new book
    """
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete a book
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### URL Configuration

```python
# urls.py
from django.urls import path
from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
```

## 3️⃣ Generic Views (Less Code!)

DRF provides generic views that handle common patterns:

```python
# views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    """
    GET: List all books
    POST: Create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a book
    PUT: Update a book
    DELETE: Delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

That's it! All CRUD operations in just a few lines!

### Available Generic Views

| View Class | HTTP Methods | Description |
|------------|--------------|-------------|
| `ListAPIView` | GET | List all objects |
| `CreateAPIView` | POST | Create object |
| `RetrieveAPIView` | GET | Get single object |
| `UpdateAPIView` | PUT, PATCH | Update object |
| `DestroyAPIView` | DELETE | Delete object |
| `ListCreateAPIView` | GET, POST | List + Create |
| `RetrieveUpdateAPIView` | GET, PUT, PATCH | Get + Update |
| `RetrieveDestroyAPIView` | GET, DELETE | Get + Delete |
| `RetrieveUpdateDestroyAPIView` | GET, PUT, PATCH, DELETE | Get + Update + Delete |

## 4️⃣ ViewSets (Most Powerful!)

ViewSets combine related views into a single class:

```python
# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing books.
    
    Provides: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

One class handles ALL CRUD operations!

### URL Configuration with Routers

```python
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
```

This automatically creates:
- `GET /books/` - List all books
- `POST /books/` - Create a book
- `GET /books/{id}/` - Retrieve a book
- `PUT /books/{id}/` - Update a book
- `PATCH /books/{id}/` - Partial update
- `DELETE /books/{id}/` - Delete a book

## 🎨 Customizing ViewSets

### Adding Custom Actions

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        """GET /books/in_stock/ - List books in stock"""
        books = self.queryset.filter(in_stock=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def mark_out_of_stock(self, request, pk=None):
        """POST /books/{id}/mark_out_of_stock/ - Mark book out of stock"""
        book = self.get_object()
        book.in_stock = False
        book.save()
        return Response({'status': 'marked out of stock'})
```

### Filtering QuerySet

```python
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    
    def get_queryset(self):
        """Filter books based on query parameters"""
        queryset = Book.objects.all()
        
        # Filter by author
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        
        return queryset
```

## 📊 Comparison Table

| Feature | Function View | APIView | Generic View | ViewSet |
|---------|--------------|---------|--------------|---------|
| Lines of code | Many | Medium | Few | Fewest |
| Customization | High | High | Medium | Medium |
| Learning curve | Low | Medium | Medium | Higher |
| DRY principle | Poor | Good | Better | Best |
| Best for | Simple/custom | Custom logic | Standard CRUD | Full APIs |

## 🧪 Testing Your API

### Using the Browsable API

1. Run your server: `python manage.py runserver`
2. Open browser to `http://localhost:8000/api/books/`
3. You'll see DRF's beautiful browsable interface!

### Using curl

```bash
# List all books
curl http://localhost:8000/api/books/

# Get single book
curl http://localhost:8000/api/books/1/

# Create book
curl -X POST http://localhost:8000/api/books/ \
     -H "Content-Type: application/json" \
     -d '{"title": "New Book", "author": "John Doe", "price": "29.99"}'

# Update book
curl -X PUT http://localhost:8000/api/books/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated Title", "author": "John Doe", "price": "39.99"}'

# Delete book
curl -X DELETE http://localhost:8000/api/books/1/
```

### Using Python requests

```python
import requests

# List all books
response = requests.get('http://localhost:8000/api/books/')
print(response.json())

# Create a book
data = {
    'title': 'Python Tricks',
    'author': 'Dan Bader',
    'price': '24.99'
}
response = requests.post('http://localhost:8000/api/books/', json=data)
print(response.json())
```

## 💪 Practice Exercise

Create a complete API for a `Product` model with:
1. List all products
2. Create a product
3. Retrieve a single product
4. Update a product
5. Delete a product
6. Custom action: Get products on sale (discount > 0)

Use ViewSet for the cleanest solution!

<details>
<summary>Solution</summary>

```python
# models.py
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)

# serializers.py
class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
    
    def get_final_price(self, obj):
        return float(obj.price) * (1 - obj.discount/100)

# views.py
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'])
    def on_sale(self, request):
        products = self.queryset.filter(discount__gt=0)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

# urls.py
router = DefaultRouter()
router.register(r'products', ProductViewSet)
urlpatterns = [path('', include(router.urls))]
```
</details>

---

**Next:** [Daily Test](./daily_test.md)
