class C2dVector():
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f"The 2d vector is {self.i}i+{self.j}j")

class vector3d(C2dVector):
    magnitude=3
    
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k
        print(f"The 3d vector is {self.i}i+{self.j}j+{self.k}k")

v1=C2dVector(1,2)
v2=vector3d(1,2,3)