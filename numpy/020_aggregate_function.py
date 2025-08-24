import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(np.sum(arr)) #output: 21
print(np.sum(arr, axis=0)) #output: [5 7 9] (sum along columns)
print(np.sum(arr, axis=1)) #output: [ 6 15] (sum along rows)
print(np.mean(arr)) #output: 3.5 (mean of all elements)
print(np.min(arr))
print(np.max(arr)) #output: 6 (maximum element)
print(np.std(arr)) #output: 1.707825127659933 (standard deviation)