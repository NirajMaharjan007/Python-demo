import numpy as np

array_3d = np.array([[[1, 2, 3], [3, 4, 5], [6, 7, 8]], [
                    [12, 13, 14], [15, 16, 17], [18, 19, 20]]])
print(array_3d)
print(array_3d.shape)


array_2d = array_3d.reshape(2, 9)
print(array_2d)
print(array_2d.shape)

array_1d = array_2d.reshape(1, 18)
print(array_1d)
print(array_1d.shape)


