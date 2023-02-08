import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
re_arr = arr.reshape(2, 3, 2)

arr_two = re_arr.reshape(2, 2, -1)
print("Array_two")
print(arr_two)
print("\nReshape, Array_two=>", arr_two.shape)
