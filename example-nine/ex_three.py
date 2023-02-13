from matplotlib.pyplot import *
from numpy import *


arr_one = array([6, 8, 9, 1, 5, 4, 8])
arr_two = array([4, 4, 6, 7, 5, 4, 9])
arr_three = array([7, 2, 0, 2, 8, 7, 0])
arr_four = array([3, 4, 8, 8, 7, 9, 3])

plot(arr_one, arr_two, color='black', marker=".", linewidth=2, linestyle="--")
show()

plot((arr_one, arr_two), (arr_three, arr_four), color="green", ms=10)
show()
