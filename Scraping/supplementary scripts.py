import numpy

# Example arrays
id1 = "BNEE844041"
val1 = [3, 22, 25, 0, 2, 2, 0, 0, 0]

# Combine the ID code and values into a single sequence (tuple or lis

# Use np.hstack to create the final array
row1 = numpy.hstack([id1] + val1)

matrix = row1

id2 = "ID2"
val2 = [1, 10, 15,  0,  0,  1,  0,  0,  0]
row2 = numpy.hstack([id2] + val2)
matrix = numpy.vstack([row1, row2])

# 'matrix' now contains the combined arrays as rows
print(matrix)
