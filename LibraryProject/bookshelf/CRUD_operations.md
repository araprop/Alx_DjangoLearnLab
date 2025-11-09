from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

from bookshelf.models import Book

# Retrieve all Book objects
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

from bookshelf.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
print(book.title)

from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
print(Book.objects.all())
