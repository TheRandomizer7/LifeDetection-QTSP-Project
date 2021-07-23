import numpy
numpy.set_printoptions(legacy='1.13')

arr1 = input().strip().split()
arr1 = numpy.array(arr1)
arr1 = arr1.astype(numpy.int64)

arr2 = input().strip().split()
arr2 = numpy.array(arr2)
arr2 = arr2.astype(numpy.int64)

print(numpy.inner(arr1, arr2))
print(numpy.outer(arr1, arr2))