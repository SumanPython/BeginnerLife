import numpy as np
#axis = 0 is columns, axis = 1 is rows
a = np.genfromtxt("data.txt", delimiter=",", dtype=int)
print(a)
print(a > 50)
b = a[a > 50]
print(b)
print(a)
c = np.any(a > 50, axis=0)
print(c)
c = np.all(a > 50, axis=0)
print(c)
g = ((a> 50) & (a < 100))
print("g = ",g)