from numpy import *

arr = array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = where(arr % 2 == 1)
print(x)

for i in arr:
    if (i % 2) == 1:
        print(i)

li = []
for index, i in ndenumerate(arr):
    # print(index, " ", i)
    if (i % 2) == 1:
        li.append(index)
a = array(li)
print(a)
print(a.reshape(-1))
