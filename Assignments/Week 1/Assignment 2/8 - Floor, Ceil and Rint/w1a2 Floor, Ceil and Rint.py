<<<<<<< HEAD
import numpy
numpy.set_printoptions(legacy='1.13')

arr = input().strip().split()
arr = numpy.array(arr)
arr = arr.astype(numpy.float64)

print(numpy.floor(arr))
print(numpy.ceil(arr))
=======
import numpy
numpy.set_printoptions(legacy='1.13')

arr = input().strip().split()
arr = numpy.array(arr)
arr = arr.astype(numpy.float64)

print(numpy.floor(arr))
print(numpy.ceil(arr))
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(numpy.rint(arr))