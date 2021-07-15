<<<<<<< HEAD
import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = input().strip().split()
polynomial = numpy.array(polynomial)
polynomial = polynomial.astype(numpy.float64)

point = int(input().strip())

=======
import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = input().strip().split()
polynomial = numpy.array(polynomial)
polynomial = polynomial.astype(numpy.float64)

point = int(input().strip())

>>>>>>> 7de5859c4234bff3b6ef6c6ddb3110f013088a9f
print(numpy.polyval(polynomial, point))