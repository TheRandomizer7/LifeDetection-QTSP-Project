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

print(arr.transpose())
print(arr.flatten())