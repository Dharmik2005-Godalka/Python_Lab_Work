import numpy as np

arr_c1 = np.array([1, 2, 3, 4, 5, 6])
arr_c2 = np.array([4, 5, 6, 7, 8])
commons = np.intersect1d(arr_c1, arr_c2)

print(commons)
