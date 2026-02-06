# Task 1: Discount Rules

try:
    order_amount = int(input("Enter order amount: "))
except ValueError:
    print("Error: Please enter a valid numeric value.")
    exit()

# Determine discount
if order_amount >= 2000:
    discount_rate = 0.15
elif order_amount >= 1500:
    discount_rate = 0.10
elif order_amount >= 1000:
    discount_rate = 0.07
else:
    discount_rate = 0.0

discount = order_amount * discount_rate
subtotal = order_amount - discount

# Optional tax
tax = subtotal * 0.05
final_total = subtotal + tax

print("Subtotal after discount:", subtotal)
print("Tax (5%):", tax)
print("Final total:", final_total)