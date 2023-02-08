import numpy as np

array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
                    [10, 11, 12], [13, 14, 15], [16, 17, 18]]])

for i in array_3d:
    print("Element of 1st element")
    for j in i:
        print("Element of 2nd element")
        for k in j:
            print("Element of 3rd element")
            print(k)


print("\n==========================================================")
for i in range(len(array_3d)):
    print("Element of 1st element", i)
    for j in range(len(array_3d[i-1])):
        print("Element of 2nd element", j)
        for k in range(len(array_3d[j-2])):
            print("Element of 3rd element", k)
            print(array_3d[i][j][k])
