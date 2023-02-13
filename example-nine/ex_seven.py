from matplotlib.pyplot import *
from numpy import *

arr_one = array([7, 2, 4, 3, 8, 5, 6])
arr_two = array([6, 9, 10, 18, 45, 65, 32])

arr_one.sort()
arr_two.sort()


bar(arr_one, arr_two, width=1.2)
show()

barh(arr_one, arr_two, height=2.6)
show()
