# Task 2: Read File in Different Ways

file = open("sales_data.txt", "r")

# Read entire file
print("Using read():")
print(file.read())

file.close()

file = open("sales_data.txt", "r")

# Read first line
print("Using readline():")
print(file.readline().strip())

file.close()

file = open("sales_data.txt", "r")

# Read all lines and convert to integers
lines = file.readlines()
sales_list = [int(line.strip()) for line in lines]

print("Using readlines():")
print(sales_list)

file.close()
