# Write a Python Class to represent a book. The Book class should have attributes:
# title, author, publisher, page count and price
# And provide a constructor method alongside appropriate getter and setter functions.

class Book:
    # Constructor method
    def __init__(self, title, author, publisher, page_count, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.page_count = page_count
        self.price = price

    # getter and setter functions
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def get_page_count(self):
        return self.page_count

    def get_price(self):
        return self.price

# If asked to create subclass
# class Subclass(Book):
#
#  def __init__(self):
#   super().__init__()
#
