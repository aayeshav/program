import numpy as np
arr=np.arange(1,21).reshape(4, 5)
print("Index of 10 in the array:", np.where(arr == 10))
print(arr)
print(arr[1, 2])  # Accessing element at row 1, column 2
print(arr[0])
print(arr[0,])
print(arr[1,2:4]) # Accessing elements from row 1, columns 2 to 3