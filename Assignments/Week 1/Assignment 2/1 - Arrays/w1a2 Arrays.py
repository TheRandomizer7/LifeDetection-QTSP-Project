import numpy

def arrays(arr):
    arr = numpy.array(arr)
    arr = arr.astype(numpy.float64)
    return arr[::-1]
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)