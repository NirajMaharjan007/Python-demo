from matplotlib.pyplot import *
from numpy import *

arr = array([8, 10, 6, 4, 14])
plot(arr, marker='o', ms=25)
show()

plot(arr, color='black', marker='o')
show()

plot(arr, color='blue', marker='*', linestyle="dashed")
show()


# => can replaced by :
plot(arr, color='green', marker='*', linestyle="dotted")
show()

plot(arr, color='pink', marker='*', linewidth=10)
show()
