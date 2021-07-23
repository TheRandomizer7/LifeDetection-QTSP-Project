import numpy
from numpy.lib.utils import safe_eval

shape_arr = input().strip().split(' ')
shape_arr = numpy.array(shape_arr)
shape_arr = shape_arr.astype(numpy.int64)

shape = tuple(shape_arr)

print(numpy.zeros(shape_arr, numpy.int64))
print(numpy.ones(shape_arr, numpy.int64))