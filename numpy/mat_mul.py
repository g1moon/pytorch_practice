import numpy as np 

A = [ 1, 0, 4,-7, 0, 4, 7, 8, 9, 4, 1, 7, 9, 4, 11, 9,-6, 0, 6, 8, 11, 3, 5, 3, 5]
B = [[1,-1,0,5,7],
     [8,6,0,1,4],
     [0,4,1,-3,5]]

A = np.array(A)
B = np.array(B)

A = A.reshape(5,5)
a = A[2]
b = B[1]

#for을 이용해서 
sum_ = 0
for i in range(len(A)):
    sum_ += (a[i]*b[i])
print(sum_)

#numpy을 이용해서
print(a@b)
