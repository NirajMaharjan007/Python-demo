from matplotlib.pyplot import *
from numpy import *

arr_one = array([7, 2, 0, 2, 8, 7, 0])
arr_two = array([3, 4, 8, 8, 7, 9, 3])

scatter(arr_two, arr_one, linewidths=1.5, marker="x")
show()
