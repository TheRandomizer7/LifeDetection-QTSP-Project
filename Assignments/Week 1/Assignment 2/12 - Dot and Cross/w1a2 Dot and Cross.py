import numpy

dimension = int(input())

arr1 = numpy.empty(dimension * dimension, numpy.int64)
arr1 = arr1.reshape(dimension, dimension)

arr2 = numpy.empty(dimension * dimension, numpy.int64)
arr2 = arr2.reshape(dimension, dimension)

i = 0
while i < dimension:
    input_column = input().strip().split()
    j = 0
    while j < dimension:
        arr1[i, j] = int(input_column[j])
        j += 1
    i += 1

i = 0
while i < dimension:
    input_column = input().strip().split()
    j = 0
    while j < dimension:
        arr2[i, j] = int(input_column[j])
        j += 1
    i += 1

outputMatrix = numpy.empty((dimension, dimension), numpy.int64)

i = 0
while i < dimension:
    j = 0
    while j < dimension:
        rowMatrix = numpy.reshape(arr1[i:i+1, 0:dimension], (dimension))
        columnMatrix = numpy.reshape(arr2[0:dimension, j:j+1], (dimension))
        outputMatrix[i, j] = numpy.dot(rowMatrix, columnMatrix)
        j += 1
    i += 1

print(outputMatrix)
