<<<<<<< HEAD
import numpy

dimensions = input().strip().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])

arr = numpy.empty(rows * columns, numpy.int64)
arr = arr.reshape(rows, columns)

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr[i, j] = int(input_column[j])
        j += 1
    i += 1

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
=======
import numpy

dimensions = input().strip().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])

arr = numpy.empty(rows * columns, numpy.int64)
arr = arr.reshape(rows, columns)

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr[i, j] = int(input_column[j])
        j += 1
    i += 1

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(round(numpy.std(arr), 11))