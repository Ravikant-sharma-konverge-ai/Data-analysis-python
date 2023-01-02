# Numpy exercise
from secrets import randbelow
import numpy as np
## Array creation
### Create a numpy array of size 10, filled with zeros.
r = np.zeros(10)

### Create a numpy array with values ranging from 10 to 49
r = np.arange(10,50)

### Create a numpy matrix of 2*2 integers, filled with ones
lst = [[1]*2]*2
r = np.array(lst)
#or
r  = np.ones([2,2], dtype=int)

### Create a numpy matrix of 3*2 float numbers, filled with ones.
r = np.ones([3,2], dtype=np.float16)

### Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.
X = np.arange(4, dtype=int)

r = np.ones_like(X)
r = np.zeros_like(X)

### Create a numpy matrix of 4*4 integers, filled with fives.
r = np.ones([4,4,],dtype=int)*5

### Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.
X = np.array([[2,3], [6,2]], dtype=int)

r = np.ones_like(X) * 7

### Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.
r = np.identity(3)
#r = np.zeros([3,3], dtype=int)
#for i in range(len(r[0])):
#    r[i,i]  = 1

### Create a numpy array, filled with 3 random integer values between 1 and 10.
r = np.random.randint(10, size=3)

### Create a 3*3*3 numpy matrix, filled with random float values.
r = np.random.randn(3,3,3)

### Given the X python list convert it to an Y numpy array
X = [1, 2, 3]

Y = np.array(X)

### Given the X numpy array, make a copy and store it on Y.
X = np.array([5,2,3], dtype=np.int)

Y = np.copy(X)

### Create a numpy array with the odd numbers between 1 to 10
r = np.arange(1,11,2)

###  Create a numpy array with numbers from 1 to 10, in descending order.
r = np.arange(1,11,-1)

### Create a 3*3 numpy matrix, filled with values ranging from 0 to 8
r = np.arange(0,9).reshape(3,3)

### Show the memory size of the given Z numpy matrix
r = Z = np.zeros((10,10))
print("%d bytes" % (Z.size * Z.itemsize))







