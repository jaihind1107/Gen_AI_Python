#Task 1
import Math_utils
from Math_utils import square

print(Math_utils.add(5, 3))  # Output: 8
print(Math_utils.subtract(10, 4))  # Output: 6
print(square(6))  # Output: 36


#Task 2
import string_utils
from string_utils import captilaized_words, reverse_string, word_count

sentence = "hello world"
print(captilaized_words(sentence))  # Output: "Hello World"
print(reverse_string(sentence))  # Output: "dlrow olleh"
print(word_count(sentence))  # Output: 2


#Task 3 and Task 4
from shop_package.billing import calculate_total, apply_tax
from shop_package.discount import apply_discount, flat_discount 

prices = [100, 200, 300]
total_price = calculate_total(*prices)
print(f"Total price before tax: {total_price}")  # Output: Total price before tax: 600

discounted_price = apply_discount(total_price, 10)  # Apply a 10% discount
print(f"Price after discount: {discounted_price}")  # Output: Price after discount: 540.0

final_price = apply_tax(discounted_price)
print(f"Final price after tax: {final_price}")  # Output: Final price after tax: 586.9

flat_discounted_price = flat_discount(total_price)  # Apply a flat discount of $50
print(f"Price after flat discount: {flat_discounted_price}")  # Output: Price after flat discount: 550


