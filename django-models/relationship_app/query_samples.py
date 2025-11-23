import os
import django
import sys

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment - use just 'settings' since it's in the root
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """
    Query all books by a specific author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")
        return []

def list_all_books_in_library(library_name):
    """
    List all books in a library
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return []

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")
        return None

def create_sample_data():
    """
    Create sample data to demonstrate the queries
    """
    # Clear existing data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()
    
    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")
    
    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    
    # Create library
    library = Library.objects.create(name="Central Public Library")
    
    # Add books to library
    library.books.add(book1, book2, book3, book4)
    
    # Create librarian
    librarian = Librarian.objects.create(name="Alice Johnson", library=library)
    
    return author1, author2, library, librarian

if __name__ == "__main__":
    print("Creating sample data...")
    author1, author2, library, librarian = create_sample_data()
    
    print("\n" + "="*50)
    print("DEMONSTRATING RELATIONSHIP QUERIES")
    print("="*50)
    
    # Query 1: All books by a specific author
    print("\n1. Query all books by a specific author:")
    query_all_books_by_author("J.K. Rowling")
    
    # Query 2: List all books in a library
    print("\n2. List all books in a library:")
    list_all_books_in_library("Central Public Library")
    
    # Query 3: Retrieve the librarian for a library
    print("\n3. Retrieve the librarian for a library:")
    get_librarian_for_library("Central Public Library")