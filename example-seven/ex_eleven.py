from numpy import *

arr_1 = array([[1, 2, 3], [4, 5, 6]])
arr_2 = array([[7, 8, 9], [10, 11, 12]])


arr = concatenate([arr_1, arr_2])
print(arr)

arr_split = array_split(arr, 3)
print(arr_split)
