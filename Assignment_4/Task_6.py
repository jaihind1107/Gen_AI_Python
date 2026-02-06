# Task 6: Safe File Reading

import os

filename = input("Enter filename to open: ")

if os.path.exists(filename):
    file = open(filename, "r")
    print(file.read())
    file.close()
else:
    print("File not found. Please check the filename.")
