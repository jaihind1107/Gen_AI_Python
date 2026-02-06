# Task 5: Product Info File

file = open("products.txt", "w")

for i in range(3):
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    file.write(f"{name} | {price}\n")

file.close()

# Read and display file
file = open("products.txt", "r")
print("Product List:")
for line in file:
    print(line.strip())
file.close()
