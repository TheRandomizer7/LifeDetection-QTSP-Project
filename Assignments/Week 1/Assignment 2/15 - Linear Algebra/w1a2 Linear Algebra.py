<<<<<<< HEAD
import numpy

dimension = int(input().strip())
arr = numpy.empty(dimension * dimension, numpy.float64)
arr = arr.reshape(dimension, dimension)

i = 0
while i < dimension:
    input_column = input().strip().split()
    j = 0
    while j < dimension:
        arr[i, j] = float(input_column[j])
        j += 1
    i += 1

=======
import numpy

dimension = int(input().strip())
arr = numpy.empty(dimension * dimension, numpy.float64)
arr = arr.reshape(dimension, dimension)

i = 0
while i < dimension:
    input_column = input().strip().split()
    j = 0
    while j < dimension:
        arr[i, j] = float(input_column[j])
        j += 1
    i += 1

>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(round(numpy.linalg.det(arr), 2))