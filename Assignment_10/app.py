import pandas as pd

marks = [78, 85, 90, 66, 72]

##Task 1
df = pd.Series(marks)
print('Series values', df.values)
print('Series Index', df.index)
print('Data type', df.dtype)

print('First Element', df[0])
print('First Element', df[3:5])