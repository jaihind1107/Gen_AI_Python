# Task 1
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers for numerator and denominator.")
else:
    print(f"The result is: {result}")
finally:
    print("Operation Complete.")



# Task 2
price = [120, 350, 'abc', 500, -200, 800]

total_price = 0
for p in price:
    try:
        if not isinstance(p, (int, float)):
            raise TypeError("Price must be a number.")
        if p < 0:
            raise ValueError("Price cannot be negative.")
        total_price += p
        
    except TypeError as e:
        continue # Skip to the next price if it's not a number
    except ValueError as e:
        continue # Skip to the next price if it's negative

print(f"The total price is: {total_price}")


# Task 3
def check_age(age): 
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120.") 
    
try:
    age = int(input("Enter your age: ")) 
    check_age(age) 
except ValueError as e: 
    print(f"Error: {e}") 
else: 
    print(f"Your age is: {age}")


# Task 4
filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        print("\nFirst 3 lines of the file:")
        for i in range(3):
            line = file.readline()
            if not line:
                break
            print(line.strip())

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied to access the file.")

finally:
    print("File operation attempted.")


# Task 5
class NegativePriceError(Exception):
    """Custom exception for negative price"""
    pass


cart = []

while True:
    user_input = input("Enter item price (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        price = float(user_input)

        if price < 0:
            raise NegativePriceError("Price cannot be negative.")

        cart.append(price)

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except NegativePriceError as e:
        print("Error:", e)


print("\nShopping Summary:")
print("Total items:", len(cart))
print("Total bill:", sum(cart))


    
    