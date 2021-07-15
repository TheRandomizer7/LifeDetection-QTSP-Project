<<<<<<< HEAD
import numpy

dimensions = input().strip().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])


arr1 = numpy.empty(rows * columns, numpy.int64)
arr1 = arr1.reshape(rows, columns)

arr2 = numpy.empty(rows * columns, numpy.int64)
arr2 = arr2.reshape(rows, columns)

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr1[i, j] = int(input_column[j])
        j += 1
    i += 1

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr2[i, j] = int(input_column[j])
        j += 1
    i += 1

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
=======
import numpy

dimensions = input().strip().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])


arr1 = numpy.empty(rows * columns, numpy.int64)
arr1 = arr1.reshape(rows, columns)

arr2 = numpy.empty(rows * columns, numpy.int64)
arr2 = arr2.reshape(rows, columns)

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr1[i, j] = int(input_column[j])
        j += 1
    i += 1

i = 0
while i < rows:
    input_column = input().strip().split()
    j = 0
    while j < columns:
        arr2[i, j] = int(input_column[j])
        j += 1
    i += 1

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2)
print(arr1 % arr2)
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(arr1 ** arr2)