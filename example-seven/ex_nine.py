import numpy as np

arr_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2 = np.array([[7, 8, 9], [10, 11, 12]])

arr = np.concatenate([arr_1, arr_2])  # axis default=0
print(arr)

print("\n")
arr_new = np.concatenate([arr_1, arr_2], axis=1)
print(arr_new)
