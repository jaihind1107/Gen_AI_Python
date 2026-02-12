class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price   # private attribute
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)
        print("----------------------")

    # Getter
    def get_price(self):
        return self.__price

    # Setter
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully")
        else:
            print("Invalid price")


# Testing
p1 = Product("Tablet", 15000, "Electronics")
p1.get_info()

p1.set_price(18000)
print("Updated Price:", p1.get_price())
