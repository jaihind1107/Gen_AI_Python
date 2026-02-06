# Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

file = open("sales_data.txt", "a")
for sale in new_sales:
    file.write(str(sale) + "\n")
file.close()

# Reopen and print updated file
file = open("sales_data.txt", "r")
lines = file.readlines()

print("Updated Sales Data:")
for line in lines:
    print(line.strip())

print("Total number of lines:", len(lines))

file.close()
