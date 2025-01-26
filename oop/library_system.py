# Base Class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the parent class' __init__ method
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the parent class' __init__ method
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library Class: Using Composition
class Library:
    def __init__(self):
        self.books = []  # A list to store books

    def add_book(self, book):
        self.books.append(book)  # Adds a Book, EBook, or PrintBook instance to the library

    def list_books(self):
        for book in self.books:
            print(book)  # Print the details of each book using __str__ method
