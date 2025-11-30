"""
API Views for Django REST Framework Tutorial
Day 15: Django REST Framework Basics

This file demonstrates three approaches:
1. Function-based views
2. Class-based APIViews
3. ViewSets with Router
"""

from rest_framework import status, viewsets, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author, Category
from .serializers import (
    BookSerializer, 
    BookListSerializer,
    BookCreateSerializer,
    BookDetailSerializer,
    AuthorSerializer,
    CategorySerializer,
)


# =============================================================================
# 1. FUNCTION-BASED VIEWS
# =============================================================================

@api_view(['GET', 'POST'])
def book_list_function(request):
    """
    Function-based view for listing and creating books.
    
    GET /api/v1/books/
    POST /api/v1/books/
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def book_detail_function(request, pk):
    """
    Function-based view for retrieving, updating, and deleting a single book.
    
    GET /api/v1/books/<pk>/
    PUT /api/v1/books/<pk>/
    PATCH /api/v1/books/<pk>/
    DELETE /api/v1/books/<pk>/
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(
            {"error": "Book not found"}, 
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =============================================================================
# 2. CLASS-BASED APIVIEW
# =============================================================================

class BookListAPIView(APIView):
    """
    Class-based view for listing and creating books.
    
    GET /api/v2/books/
    POST /api/v2/books/
    """
    
    def get(self, request):
        """List all books"""
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Create a new book"""
        serializer = BookCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    """
    Class-based view for retrieving, updating, and deleting a single book.
    
    GET /api/v2/books/<pk>/
    PUT /api/v2/books/<pk>/
    DELETE /api/v2/books/<pk>/
    """
    
    def get_object(self, pk):
        """Helper method to get book or None"""
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None
    
    def get(self, request, pk):
        """Retrieve a book"""
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        """Update a book"""
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """Delete a book"""
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =============================================================================
# 3. GENERIC VIEWS (Less code!)
# =============================================================================

class BookListGeneric(generics.ListCreateAPIView):
    """
    Generic view for listing and creating books.
    Handles GET (list) and POST (create) automatically!
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic view for retrieving, updating, and deleting a book.
    Handles GET, PUT, PATCH, DELETE automatically!
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# =============================================================================
# 4. VIEWSETS (Most powerful - combines all operations!)
# =============================================================================

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model.
    
    Automatically provides:
    - list:    GET /api/v4/books/
    - create:  POST /api/v4/books/
    - retrieve: GET /api/v4/books/<pk>/
    - update:  PUT /api/v4/books/<pk>/
    - partial_update: PATCH /api/v4/books/<pk>/
    - destroy: DELETE /api/v4/books/<pk>/
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_serializer_class(self):
        """
        Use different serializers for different actions
        """
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'create':
            return BookCreateSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer
    
    def get_queryset(self):
        """
        Optionally filter queryset based on query params
        """
        queryset = Book.objects.all()
        
        # Filter by author name
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__icontains=author)
        
        # Filter by in_stock
        in_stock = self.request.query_params.get('in_stock')
        if in_stock is not None:
            queryset = queryset.filter(in_stock=(in_stock.lower() == 'true'))
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def in_stock(self, request):
        """
        Custom action: GET /api/v4/books/in_stock/
        Returns only books that are in stock
        """
        books = self.queryset.filter(in_stock=True)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def out_of_stock(self, request):
        """
        Custom action: GET /api/v4/books/out_of_stock/
        Returns only books that are out of stock
        """
        books = self.queryset.filter(in_stock=False)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def toggle_stock(self, request, pk=None):
        """
        Custom action: POST /api/v4/books/<pk>/toggle_stock/
        Toggles the in_stock status
        """
        book = self.get_object()
        book.in_stock = not book.in_stock
        book.save()
        return Response({
            'status': 'success',
            'in_stock': book.in_stock
        })


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Author model.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Category model.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
