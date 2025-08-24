import numpy as np
arr=np.array([1, 2, 3, 4, 5])
mask= arr > 3
print(mask) #output: [False False False  True  True]
print(arr[mask])  # Accessing elements where mask is True [4, 5]
             