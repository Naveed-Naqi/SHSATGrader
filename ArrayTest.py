import numpy as np

rows = 3
cols = 2

test_array = [1,2,3,4,5,6]

a = np.array(test_array).reshape(3,2)
a = a.transpose()

for x in a:
    print(x, sep=" ")