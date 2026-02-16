import numpy as np
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

average_sales = np.mean(sales)

print("Total Weekly Sales:", np.sum(sales))
print("Average Daily Sales:", average_sales)
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))
print("Standard Deviation:", np.std(sales))
print("Days with Above Average Sales:", sales[sales > average_sales])
