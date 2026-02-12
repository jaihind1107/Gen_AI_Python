class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)
        print("----------------------")

    # Optional
    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        return self.price - discount_amount


# Creating objects
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Headphones", 2000, "Accessories")

p1.get_info()
p2.get_info()

print("Discounted Price:", p1.apply_discount(10))
