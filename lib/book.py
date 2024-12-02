class Book:
    def __init__(self, title, author, genre, page_count, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.page_count = page_count  # Page count should be an integer
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Price must be positive.")

    def apply_discount(self, percentage):
        self._price -= self._price * (percentage / 100)

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
            raise ValueError("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
