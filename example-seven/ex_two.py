import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
re_arr = arr.reshape(2, 3, 2)
print(re_arr)

print("--------------------------------")
for i in range(len(re_arr)):
    print(str(i) + ", Element")
    print(re_arr[i])
