import numpy as np

array_3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
                    [10, 11, 12], [13, 14, 15], [16, 17, 18]]])


array_2d = array_3d.reshape(2, 9)

for i in np.nditer(array_3d):
    print(i)

array_1d = np.array([[1, 2, 3, 4, 5, 6]])

print("-----------------------------------------")
for i in np.nditer(array_1d):
    print(i)

print("\n-----------------------------------------")
for index, i in enumerate(array_3d):
    print(index, "\n", i)

print("\n-----------------------------------------")
for index, i in enumerate(array_2d):
    print(index, "\n", i)

print("\n-----------------------------------------")
