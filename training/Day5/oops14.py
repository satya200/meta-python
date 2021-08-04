
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

    def del_price(self):
        self.__price = 0

    def __del__(self):
        print("destructor called...")

    # property(getter, setter, deleter)
    price = property(get_price, set_price, del_price)

p1 = Product(50)

x = p1.price
p1.price = 500

print(x)
print(p1.price)
del p1.price
print(p1.price)
p2 = Product(100)
p3 = Product(400)
