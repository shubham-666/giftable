class Book:
    count = 0

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Book.count += 1

    def discount(self):
        self.price = self.price * 0.90
        print(self.title, "new price:", self.price)


book1 = Book("Python Basics", 500)
book2 = Book("Java Programming", 800)
book3 = Book("DSA Guide", 1000)

book1.discount()
book2.discount()
book3.discount()

print("Number of books created:", Book.count)