import numpy as np

# create a default 1-D array of integers
array1 = np.array([6, 7, 8, 10, 13])

# create a 1-D array of 32-bit integers 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)

# use of itemsize to determine size of each array element of array1 and array2
print(array1.itemsize)  # prints 8
print(array2.itemsize)  # prints 4
