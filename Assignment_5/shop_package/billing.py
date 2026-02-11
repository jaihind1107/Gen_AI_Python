def calculate_total(*prices):
    """Calculate the total price by summing up all the prices."""
    total_price = sum(prices)
    return total_price
    
def apply_tax(price):
    """Calculate the tax amount based on the price and tax rate."""
    tax_rate = 8.5  # Example tax rate of 8.5%
    tax_amount = price * (tax_rate / 100)
    return price + tax_amount