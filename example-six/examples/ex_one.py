import numpy as np

li = [1, 2, 3]
arr = np.array(li)

print(type(li), li)
print(type(arr), arr)

one_dimensional = np.array([1, 2, 3, 4])
two_dimensional = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
three_dimensional = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])

print(one_dimensional.ndim)
print(two_dimensional.ndim)
print(three_dimensional.ndim)

# Array indexing to access the specific element
print("------------------------------------------")
arr = np.array([[[1, 2, 3], [4, 5, 6],], [[7, 8, 9], [10, 11, 12]]])
print(arr.ndim)
print(arr[0, 1, 2])
