import numpy as np

li = []

for i in range(12):
    li.append(int(input("Enter a number for: "+str(i) + " => ")))

arr = np.array(li)


arr_2d = arr.reshape(-1, 6)
print(arr_2d)

for i in np.nditer(arr_2d[:, ::2]):
    print(i)
