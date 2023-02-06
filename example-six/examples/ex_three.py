import numpy as np
li = [1, 2, 3]
arr = np.array(li)

arr_copy = arr.copy()  # ==> no changes
arr_2 = arr  # ==> changes
arr_view = arr_copy.view()  # ==> shows original array

arr[1] = 6

print("arr =>", arr)
print("arr_2 =>", arr_2)
print("arr_copy =>", arr_copy)
print("arr_view =>", arr_view)

print("arr_view.base =>", arr_view.base)
print("arr_view.base =>", arr_copy.base)
