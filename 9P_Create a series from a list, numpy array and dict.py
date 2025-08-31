import pandas as pd  

list_series = pd.Series([10, 20, 30])

import numpy as np
array_series = pd.Series(np.array([1, 2, 3, 4]))

dict_series = pd.Series({'x': 5, 'y': 10, 'z': 15})

print("List Series:\n", list_series)
print("Array Series:\n", array_series)
print("Dict Series:\n", dict_series)
