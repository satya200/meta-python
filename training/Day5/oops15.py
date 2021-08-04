
class Product:

    def __init__(self,  price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if (val < 0):
            print(f"Price cannot be negative :{val}")
        else:
            self.__price = val

    @price.deleter
    def price(self):
        self.__price = 0

    # property(getter, setter, deleter)
    # price = property(get_price, set_price, del_price)

p1 = Product(50)

print(p1.price)
p1.price = 500
print(p1.price)
