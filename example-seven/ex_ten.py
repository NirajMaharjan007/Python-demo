import numpy as np

arr_1 = np.array([[1, 2, 3], [4, 5, 6]])
arr_2 = np.array([[7, 8, 9], [10, 11, 12]])

arr_dstack = np.dstack([arr_1, arr_2])
arr_hstack = np.hstack([arr_1, arr_2])
arr_vstack = np.vstack([arr_1, arr_2])
arr_stack = np.stack([arr_1, arr_2])

print("Array hstack,\n", arr_hstack)
print("\n")
print("Array stack\n", arr_stack)
print("\n")
print("Array vstack,\n", arr_vstack)
print("\n")
print("Array dstack,\n", arr_dstack)
