import numpy as np

arr_mem = np.array([1, 2, 3, 4, 5], dtype=np.int64)
total_bytes = arr_mem.size * arr_mem.itemsize

print(total_bytes)
