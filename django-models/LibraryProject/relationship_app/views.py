from django.shortcuts import render
from .models import Book, Library, Author
from django.views.generic import DetailView
# Create your views here.

def list_books(request):
    """Function that lists all books with their authors"""
    #1. get all the books
    all_books = Book.objects.all()

    #2. send the books to the template
    return render(request, 'list_books.html', {'books' : all_books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'