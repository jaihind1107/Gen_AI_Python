class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(self.name, self.price)


class Laptop(Product):
    def get_info(self):
        print("Laptop ->", self.name, "| Price:", self.price)


class Mobile(Product):
    def get_info(self):
        print("Mobile ->", self.name, "| Price:", self.price)


l1 = Laptop("Dell", 60000)
m1 = Mobile("iPhone", 80000)

products = [l1, m1]

for item in products:
    item.get_info()   # Polymorphism in action
