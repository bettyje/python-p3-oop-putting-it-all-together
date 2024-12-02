class Shoe:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self._price = price
        self.condition = 'New'

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
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            raise ValueError("size must be an integer")

    def repair(self):
        self.condition = 'Repaired'
        print("The shoe has been repaired.")
