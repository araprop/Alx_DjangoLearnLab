from django.urls import path
from . import views

urlpatterns = [
    # Route for books list (function view)
    path('books/', views.list_books, name='book_list'),
    
    # Route for library details (class view)
    # <int:pk> means "expect a number, call it 'pk' (primary key)"
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]