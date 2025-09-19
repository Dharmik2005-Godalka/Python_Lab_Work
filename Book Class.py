class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        self.price -= discount

# Create two books
book1 = Book("Python Programming", "John Smith", 500)
book2 = Book("OOP with Python", "Jane Doe", 600)

# Display details
book1.display()
book2.display()

# Apply 10% discount to book2
book2.apply_discount(10)

print("\nAfter applying 10% discount:")
book2.display()
