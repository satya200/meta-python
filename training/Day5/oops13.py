
class Product:

    def __init__(self,  price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, val):
        if (val < 0):
            print(f"Price cannot be negative :{val}")
        else:
            self.__price = val

p1 = Product(50)
print(p1.get_price())

p1.set_price(-10)
print(p1.get_price())
