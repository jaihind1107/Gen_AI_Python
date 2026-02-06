# -----------------------------
# Task 1: Basic Function - Price After Discount
# -----------------------------

def apply_discount(price, discount_percent=5):
    # Ensure discount does not exceed 60%
    if discount_percent > 60:
        discount_percent = 60

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


# Testing Task 1
print(apply_discount(1000, 10))   # Expected: 900
print(apply_discount(500))        # Expected: 475 (default 5%)


# -----------------------------
# Task 2: Recursive Function - Factorial
# -----------------------------

def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Testing Task 2
print(factorial(5))    # Expected: 120
print(factorial(0))    # Expected: 1
print(factorial(-3))   # Error message


# -----------------------------
# Task 3: Lambda Function - GST Calculator
# -----------------------------

gst = lambda price: price + (0.18 * price)

print(gst(100))  # Expected: 118.0


# Extra: GST + Discount together
final_price = lambda price, discount=0: (price + 0.18 * price) - (price * discount / 100)

print(final_price(1000, 10))  # GST + 10% discount


# -----------------------------
# Task 4: Using map() - Apply GST to List
# -----------------------------

prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)


# -----------------------------
# Task 5: Using filter() - Filter Expensive Products
# -----------------------------

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda x: x > 500, prices))
less_or_equal_500 = list(filter(lambda x: x <= 500, prices))

print("Prices > 500:", greater_than_500)
print("Prices <= 500:", less_or_equal_500)


# -----------------------------
# Task 6: Combined Utility Function
# -----------------------------

def process_prices(prices):
    # Apply 10% discount
    discounted_prices = list(map(lambda x: x * 0.9, prices))

    # Keep prices above 300
    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))

    return discounted_prices, filtered_prices


# Testing Task 6
discounted, filtered = process_prices([100, 500, 900, 50, 750])
print("Discounted prices:", discounted)
print("Filtered prices (>300):", filtered)


# -----------------------------
# Task 7: Mini Problem - Menu Using Functions
# -----------------------------

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return None
    return max(prices_list)


prices_list = []

while True:
    print("\nMenu:")
    print("1 → Add price")
    print("2 → Show average price")
    print("3 → Show highest price")
    print("q → Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices_list, price)
        print("Price added.")

    elif choice == "2":
        avg = get_average_price(prices_list)
        print("Average price:", avg)

    elif choice == "3":
        max_price = get_max_price(prices_list)
        if max_price is None:
            print("No prices available.")
        else:
            print("Highest price:", max_price)

    elif choice.lower() == "q":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")