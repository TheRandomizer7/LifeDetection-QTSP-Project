import numpy

arr = input().strip().split(' ')
arr = numpy.array(arr)
arr = arr.astype(numpy.int64)
arr = numpy.reshape(arr, (3, 3))

print(arr)