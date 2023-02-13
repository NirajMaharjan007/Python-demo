from matplotlib.pyplot import *
from numpy import *

arr_one = array([7, 2, 4, 2, 8, 7, 6])
arr_two = array([3, 4, 8, 8, 7, 9, 3])

arr_one.sort()
arr_two.sort()

bar(arr_one, arr_two)
show()
