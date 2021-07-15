import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = input().strip().split()
polynomial = numpy.array(polynomial)
polynomial = polynomial.astype(numpy.float64)

point = int(input().strip())

print(numpy.polyval(polynomial, point))