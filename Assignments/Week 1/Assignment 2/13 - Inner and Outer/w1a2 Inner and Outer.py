<<<<<<< HEAD
import numpy
numpy.set_printoptions(legacy='1.13')

arr1 = input().strip().split()
arr1 = numpy.array(arr1)
arr1 = arr1.astype(numpy.int64)

arr2 = input().strip().split()
arr2 = numpy.array(arr2)
arr2 = arr2.astype(numpy.int64)

print(numpy.inner(arr1, arr2))
=======
import numpy
numpy.set_printoptions(legacy='1.13')

arr1 = input().strip().split()
arr1 = numpy.array(arr1)
arr1 = arr1.astype(numpy.int64)

arr2 = input().strip().split()
arr2 = numpy.array(arr2)
arr2 = arr2.astype(numpy.int64)

print(numpy.inner(arr1, arr2))
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(numpy.outer(arr1, arr2))