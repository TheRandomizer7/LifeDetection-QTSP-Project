import numpy
numpy.set_printoptions(legacy='1.13')

arr = input().strip().split()
arr = numpy.array(arr)
arr = arr.astype(numpy.float64)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))