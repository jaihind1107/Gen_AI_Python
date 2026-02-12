class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.price} - {self.category}"

    def __add__(self, other):
        return self.price + other.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Product removed")
                break

    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_all_products(self):
        for product in self.products:
            print(product)


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self, name, price, category):
        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print("Store:", self.store_name)
        print("Total Products:", len(self.inventory.products))
        print("Total Value:", self.inventory.get_total_value())


# Testing System
store = Store("Tech World")

store.add_new_product("Laptop", 50000, "Electronics")
store.add_new_product("Mobile", 30000, "Electronics")
store.add_new_product("Keyboard", 2000, "Accessories")

store.inventory.show_all_products()
store.show_summary()

# Using operator overloading
p1 = store.inventory.products[0]
p2 = store.inventory.products[1]

print("Combined Price:", p1 + p2)
