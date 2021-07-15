<<<<<<< HEAD
import numpy
from numpy.lib.utils import safe_eval

shape_arr = input().strip().split(' ')
shape_arr = numpy.array(shape_arr)
shape_arr = shape_arr.astype(numpy.int64)

shape = tuple(shape_arr)

print(numpy.zeros(shape_arr, numpy.int64))
=======
import numpy
from numpy.lib.utils import safe_eval

shape_arr = input().strip().split(' ')
shape_arr = numpy.array(shape_arr)
shape_arr = shape_arr.astype(numpy.int64)

shape = tuple(shape_arr)

print(numpy.zeros(shape_arr, numpy.int64))
>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(numpy.ones(shape_arr, numpy.int64))