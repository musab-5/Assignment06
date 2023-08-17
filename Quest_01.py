class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")


class Member(Person):
    def __init__(self, name, age, member_id):
        super().__init__(name, age)
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book_title):
        self.books_borrowed.append(book_title)
        print(f"{self.name} borrowed '{book_title}'")

    def display_books_borrowed(self):
        print(f"{self.name}'s Borrowed Books:")
        for book in self.books_borrowed:
            print(book)


class Librarian(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def add_book(self, book_title):
        print(f"{self.name} added '{book_title}' to the library")


# Create a Member
member = Member("Alice", 25, "M001")
member.display_info()
member.borrow_book("Introduction to Python")
member.borrow_book("Data Structures and Algorithms")
member.display_books_borrowed()
print()

# Create a Librarian
librarian = Librarian("John", 30, "L001")
librarian.display_info()
librarian.add_book("Python Cookbook")
