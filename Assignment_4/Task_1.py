# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Write each sale on a new line
file = open("sales_data.txt", "w")
for sale in sales:
    file.write(str(sale) + "\n")
file.close()

# Reopen and print contents
file = open("sales_data.txt", "r")
print("Sales Data (Line by Line):")
print(file.read())
file.close()
