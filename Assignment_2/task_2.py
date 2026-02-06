# Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_orders = 0

print("Order Amount -> Discount % -> Final Amount")

for order in orders:
    if order >= 2000:
        discount_rate = 0.15
    elif order >= 1500:
        discount_rate = 0.10
    elif order >= 1000:
        discount_rate = 0.07
    else:
        discount_rate = 0.0

    if discount_rate > 0:
        discounted_orders += 1

    final_amount = order - (order * discount_rate)
    total_revenue += final_amount

    print(order, "->", int(discount_rate * 100), "% ->", final_amount)

print("Total revenue after discounts:", total_revenue)
print("Orders that received a discount:", discounted_orders)