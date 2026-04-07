class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Issued"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Catalog:")
            for book in self.books:
                print(book)

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' has been issued.")
                return
        print("Book not available or ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_available:
                book.is_available = True
                print(f"Book '{book.title}' has been returned.")
                return
        print("Invalid return request.")


# ----------- Main Program -----------
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        library.add_book(Book(title, author, isbn))

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        isbn = input("Enter ISBN of book to issue: ")
        library.issue_book(isbn)

    elif choice == "4":
        isbn = input("Enter ISBN of book to return: ")
        library.return_book(isbn)

    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
