import numpy as np 

A = [ 1, 0, 4,-7, 0, 4, 7, 8, 9, 4, 1, 7, 9, 4, 11, 9,-6, 0, 6, 8, 11, 3, 5, 3, 5]
B = [[1,-1,0,5,7],
     [8,6,0,1,4],
     [0,4,1,-3,5]]

while len(A) != 15:
    A.pop()

A = np.array(A)
C = A.reshape(5,3)

X = C.T * B
print(X)
