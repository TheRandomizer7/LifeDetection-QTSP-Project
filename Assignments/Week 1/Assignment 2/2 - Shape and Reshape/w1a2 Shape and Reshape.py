<<<<<<< HEAD
import numpy

arr = input().strip().split(' ')
arr = numpy.array(arr)
arr = arr.astype(numpy.int64)
arr = numpy.reshape(arr, (3, 3))

=======
import numpy

arr = input().strip().split(' ')
arr = numpy.array(arr)
arr = arr.astype(numpy.int64)
arr = numpy.reshape(arr, (3, 3))

>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(arr)