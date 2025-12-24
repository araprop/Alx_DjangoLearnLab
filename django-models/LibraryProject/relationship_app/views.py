# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view - SIMPLE VERSION
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    # This automatically makes the library object available in template
    # The template can access books using library.books.all()