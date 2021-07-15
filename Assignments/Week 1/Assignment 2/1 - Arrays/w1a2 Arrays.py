<<<<<<< HEAD
import numpy

def arrays(arr):
    arr = numpy.array(arr)
    arr = arr.astype(numpy.float64)
    return arr[::-1]
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
=======
import numpy

def arrays(arr):
    arr = numpy.array(arr)
    arr = arr.astype(numpy.float64)
    return arr[::-1]
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(result)