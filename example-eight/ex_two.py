from numpy import *

li = [1, 8, 3, 6, 8, 9]
arr = array(li)
arr.sort()

li.reverse()
rev_array = array(li)

print(arr)

# for i in range(len(arr)-1, -1, -1):
#     print(arr[i], end=" ")

print(rev_array)


x = [True, False, False, True, False, True]
new_arr = arr[x]
print(new_arr)

arr_one = (arr % 2) == 1
print(arr_one)
