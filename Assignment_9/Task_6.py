import numpy as np
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
sorted_marks = np.sort(marks)
average_marks = np.mean(marks)

print("Sorted Marks:", sorted_marks)
print("25th Percentile:", np.percentile(marks, 25))
print("50th Percentile (Median):", np.percentile(marks, 50))
print("75th Percentile:", np.percentile(marks, 75))
print("Students Above Average:", np.sum(marks > average_marks))
