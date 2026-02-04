
# Task 1: Working with Lists and Tuples
products = ["apple", "banana", "orange", "tomato", "potato", "cucumber", "rice", "bread"]
sample_product = ("apple", 100, "Fruit")

print(f"Second Product: {products[1]}")
print(f"Last Products: {products[-1]}")

products.append("watermelon")
products.append("pineapple")

print(f"All Products after addition: {products}")

sample_product_list = list(sample_product)
sample_product_list[1] = 120
sample_product = tuple(sample_product_list)
print(f"Updated Sample Product: {sample_product}")


# Task 2: Working with sets
categories = [
    "Fruit",
    "Fruit",
    "Fruit",
    "Vegetable",
    "Vegetable",
    "Vegetable",
    "Grocery",
    "Grocery"
]
categories_set = set(categories)    # Create a set of categories
print("Categories set:", categories_set)


categories_set.add("Electronics")   # Add a new category and show duplicates are ignored
categories_set.add("Vegetable")  # duplicate
print("After adding categories:", categories_set)

print("Is 'Grocery' in categories_set?", "Grocery" in categories_set)  #Check if a category exists

print("Total unique categories:", len(categories_set))   # Extra (optional): Number of unique categories


# Task 3 : Working with Dictionaries
price_dict = {
    "apple": 100,
    "banana": 50,
    "orange": 80,
    "tomato": 40,
    "potato": 30,
    "cucumber": 60,
    "rice": 200,
    "bread": 150
}

price_dict["watermelon"] = 120
price_dict["apple"] = 150
price_dict["banana"] = 70
price_dict["orange"] = 100
price_dict["tomato"] = 50
price_dict["potato"] = 40
price_dict["cucumber"] = 70
price_dict["rice"] = 250
price_dict["bread"] = 180

if "banana" in price_dict:
    del price_dict["banana"] #remove banana


total_price = sum(price_dict.values())
average_price = total_price / len(price_dict)
print(f"Average price of products: {average_price}")

#max and min price products
max_price_product = max(price_dict, key=price_dict.get)
min_price_product = min(price_dict, key=price_dict.get)
print(f"Product with highest price: {max_price_product} at {price_dict[max_price_product]}")
print(f"Product with lowest price: {min_price_product} at {price_dict[min_price_product]}")


# Task 4 : Combined Operations

# 1. Create catalog as a list of tuples (product_name, price, category)
catalog = []

for product, category in zip(products, categories):
    if product in price_dict:   # ensure product has a price
        catalog.append((product, price_dict[product], category))

print("Catalog:", catalog)


# 2. Create a dictionary mapping category -> list of product names
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)

print("Category to Products:", category_to_products)


# 3. Find the category with the maximum number of products (NO lambda)
max_category = None
max_count = 0

for category in category_to_products:
    count = len(category_to_products[category])
    if count > max_count:
        max_count = count
        max_category = category

print("Category with maximum products:", max_category)
print("Products in this category:", category_to_products[max_category])