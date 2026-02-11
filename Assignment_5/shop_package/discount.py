def apply_discount(price, discount_percent):
    """Apply a discount to the price and return the discounted price."""
    discount_amount = price * (discount_percent / 100)
    discounted_price = price - discount_amount
    return discounted_price

def flat_discount(price):
    """Apply a flat discount to the price and return the discounted price."""
    discount_amount = 50
    discounted_price = price - discount_amount
    return max(discounted_price, 0)  # Ensure the price doesn't go below 0