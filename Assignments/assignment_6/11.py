class Book:
    total_Books = 0
    def incrememt_Books(self):
        Book.total_Books += 1
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.incrememt_Books()


b1= Book("Harry-Porter", "Harry ")
Printer = print(b1.title, b1.author, Book.total_Books)
