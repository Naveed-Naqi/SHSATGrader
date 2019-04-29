test = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

test2 = test[1:][2:]

print(test2)

"""

Count the number of 1s in the matrix 

if decimal is in col 0: divide it the answer by the number of 1s in the matrix

if decimal is in col 1: divide it the answer by the (number of 1s in the matrix) - 1

if decimal is in col 2: divide it the answer by the (number of 1s in the matrix) - 2

"""