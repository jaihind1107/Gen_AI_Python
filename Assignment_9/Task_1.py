import numpy as np

# 1D array from 1 to 10
arr_1d = np.arange(1, 11)

# 2D array of shape (3, 3) with values 1 to 9
arr_2d = np.arange(1, 10).reshape(3, 3)

# Array from a Python list
arr_list = np.array([10, 20, 30, 40, 50])

# Print shape and data type
print("1D Array:", arr_1d)
print("Shape:", arr_1d.shape, "Data Type:", arr_1d.dtype)

print("\n2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape, "Data Type:", arr_2d.dtype)

print("\nList Array:", arr_list)
print("Shape:", arr_list.shape, "Data Type:", arr_list.dtype)
