import numpy

dimensions = input().strip().split(' ')
rows1 = int(dimensions[0])
rows2 = int(dimensions[1])
columns = int(dimensions[2])


arr1 = numpy.empty(rows1 * columns, numpy.int64)
arr1 = arr1.reshape(rows1, columns)

arr2 = numpy.empty(rows2 * columns, numpy.int64)
arr2 = arr2.reshape(rows2, columns)

i = 0
while i < rows1:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr1[i, j] = int(input_column[j])
        j += 1
    i += 1

i = 0
while i < rows2:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr2[i, j] = int(input_column[j])
        j += 1
    i += 1

print(numpy.concatenate((arr1, arr2), axis = 0))