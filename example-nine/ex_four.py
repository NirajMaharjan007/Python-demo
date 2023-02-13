from matplotlib.pyplot import *
from numpy import *

arr_one = array([6, 8, 9, 1, 5, 4, 8])
arr_two = array([4, 3, 6, 7, 8, 12, 9])

arr_one.sort()
arr_two.sort()

xlabel("array_one")
ylabel("array_two")
title("Title")
grid(True, color="gray", linewidth=0.5, linestyle="dashed")
plot(arr_one, arr_two, color="green")
show()
