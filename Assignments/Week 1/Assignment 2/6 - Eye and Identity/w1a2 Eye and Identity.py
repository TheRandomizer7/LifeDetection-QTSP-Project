import numpy
numpy.set_printoptions(legacy='1.13')

dimensions = input().strip().split(' ')
rows = int(dimensions[0])
columns = int(dimensions[1])

print (numpy.eye(rows, columns, k = 0))
