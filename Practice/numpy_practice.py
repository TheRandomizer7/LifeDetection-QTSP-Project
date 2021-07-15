import numpy as np

a = np.array([1, 2, 3])
print(a)

a = np.zeros(4)
print(a)

a = np.ones(5)
print(a)

a = np.empty(6)
print(a)

a = np.arange(2, 9, 2)
print(a)

a = np.arange(2.0, 8.6, 1.8, dtype = np.int64)
print(a)

a = np.array([2, 1, 5, 3, 7, 4, 6, 8])
a = np.sort(a)
print(a)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.concatenate((a, b))
print(c)

a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0 ,1 ,2, 3], [4, 5, 6, 7]]])
print(a.ndim)
print(a.size)
print(a.shape)

a = a.reshape(24)
print(a)

a = a[:, np.newaxis]
print(a)

a = a.reshape(24)
print(a[1])
print(a[0:2])