import numpy as np 

A = [ 1, 0, 4,-7, 0, 4, 7, 8, 9, 4, 1, 7, 9, 4, 11, 9,-6, 0, 6, 8, 11, 3, 5, 3, 5]
B = [[1,-1,0,5,7],
     [8,6,0,1,4],
     [0,4,1,-3,5]]

#stack
stid = '201550031'

class Stack:
    def __init__(self, stid, mat):
        self.mat = mat
        self.stid = stid
     
    def isEmpty( self ): return len(self.top) == 0
    def size( self ): return len(self.top)
    def clear( self ): self.top = []	
    def appendStid(self,mat,stid):
        for num in stid:
            mat.append(int(num))


    def pop(self ):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self ):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self ):
        pass

instance = Stack(stid, A)
instance.appendStid(A,stid)
print(instance.mat)
