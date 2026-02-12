class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    # Magic Method
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    # Operator Overloading
    def __add__(self, other):
        return self.price + other.price


p1 = Product("Camera", 30000, "Electronics")
p2 = Product("Tripod", 5000, "Accessories")

print(p1)  # __str__
print("Total Price:", p1 + p2)  # __add__
