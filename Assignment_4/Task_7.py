# Task 7: Discount Report Mini Project

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percent = float(input("Enter discount percentage: "))

file = open("discount_report.txt", "w")

file.write("Product | Original Price | Discounted Price\n")

discounted_prices = []

for product, price in prices.items():
    discounted_price = price - (price * discount_percent / 100)
    discounted_prices.append(discounted_price)
    file.write(f"{product} | {price} | {discounted_price}\n")

# Extra summary
file.write("\n")
file.write(f"Total Items: {len(prices)}\n")
file.write(f"Average Discounted Price: {sum(discounted_prices) / len(discounted_prices)}\n")

file.close()

# Read and print report
file = open("discount_report.txt", "r")
print(file.read())
file.close()
