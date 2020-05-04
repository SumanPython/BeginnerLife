from random import *
import numpy
# a = numpy.random.rand(2, 2)
# print(a)
# a = numpy.zeros([2, 3, 4])
# print(a)
# a = numpy.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#              ,[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
# #              ,[[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]]])
# # print(a)
# # print(a[2, 2, 1:3])
# # x = numpy.random.randint(1, 100, (3,3), dtype=int)
# # print(x)
# # print(numpy.identity(3))
# print(50 * "0")
# array1 = numpy.array([[[1, 2, 3],[4, 5, 6], [7, 8, 9]],
#                       [[1, 2, 3],[4, 5, 6], [7, 8, 9]],
#                       [[1, 2, 3],[4, 5, 6], [7, 8, 9]]])
# r1 = numpy.repeat(array1, 2, axis=0)
# print(r1)
# print(50 * "1")
# r2 = numpy.repeat(array1, 2, axis=1)
# print(r2)
# r3 = numpy.repeat(array1, 2, axis=2)
# print(r3)


# array2 = numpy.array([[1, 2, 3],[1,4, 5, 6], [7, 8, 9]], 2, axis = 1)
# print(array2)
# array3 = numpy.array([[1, 2, 3],[1,4, 5, 6], [7, 8, 9]], 2, axis = 2)
# print(array3)
a = numpy.array([1, 2, 3])
print(a)
b = a.copy()
print(b)
b[0] = 100
print(b)
print(a)

