import numpy
# import sys
# #print(numpy.array([1, 2, 3]))
# # a = numpy.array([1, 2, 3])
# # b = numpy.array([4, 5, 6])
# # c = a * b
# # print(c)
# a = numpy.array([[1, 2.0, "Suman", [1, 2]],
#                 [1, 2, 3, 4]])
# b = numpy.array([[1.0, 1, 3], [1.3, 1, "suman"]])
# print("print array", a)
# #to print dimension of array
# print("size of np array dimension is ",a.ndim)
# #to print the shape of array
# print("hape of nparray is ",a.shape)
# #to get type of nparray
# print("type is ",a.dtype)
# #to get the number of elements in np array
# print("size is ",a.size)
# #to get the size of float
# print("size of float ", b.size)
# #to get the amount of memory
# print(a.nbytes)
# first = numpy.array([[1, 2, 3, 1.1], [1, 2, 3, 4]])
# print(first.size)
# a = numpy.array([[1, 2.0, "a"],
#                 [1.0, 2, 3, "Suman"]])
# b = numpy.array([[[1.0, 99, 7], 1, 3, 1], [1.3, 1, "a", 7]])
# #size for number of elements in the array
# print(a.size)
# print(b.size)
# #to get to print the number of bytes, by default 32
# print(a.nbytes)
# #type of the elements
# print(a.dtype)
# print(b.dtype)
# a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# #size for number of elements in the array
# print(a.size)
# #to get the shape of elements
# print(a.shape)
# #to get the data type of elements
# print(a.dtype)
# #to get the memory size used, each element uses 4 bytes for int
# print(a.nbytes)
# a = numpy.array(["Suman Palisetty"])
# print(a.nbytes)
# a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# #to choose a specific element from the list use a[row, col] with index in mind
# print(a)
# print(a[1, 5])
# print(a[1, -5])
# #to get the first row
# print(a[0, :])
# #to get a specific column of 3 and 10 from 'a'
# print(a[:,2])
# a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# #slicing on the first row
# print(a[0, 1:5:3])
# #slicing in negative index
# a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a[1, -1:4:-2])
# print(a[0, 1:-2:2])
# print(a[0, 1:-1:2])
x = numpy.array([[0, 11, 22, 33, 44, 55, 66, 77, 88, 99], [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]])
print(x)
print(x[0, -1:2:-1])
print(x[1, 1:7])
print(x[0, -1:2:-2])






