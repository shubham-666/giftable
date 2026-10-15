class Book:
    def __init__(self, title, author, copies=1):
        if not title.strip() or not author.strip():
            raise ValueError("Title and author are required.")
        if not isinstance(copies, int) or copies < 0:
            raise ValueError("Copies must be a non-negative integer.")
        self.title = title.strip()
        self.author = author.strip()
        self.__copies = copies

    @property
    def copies(self):
        return self.__copies

    def add_copies(self, count):
        if not isinstance(count, int) or count < 1:
            raise ValueError("Count must be a positive integer.")
        self.__copies += count

    def borrow(self):
        if self.__copies <= 0:
            return False
        self.__copies -= 1
        return True

    def return_book(self):
        self.__copies += 1

    def to_dict(self):
        return {"title": self.title, "author": self.author, "copies": self.__copies}

    def __str__(self):
        return f"{self.title} by {self.author} ({self.__copies} copies)"
