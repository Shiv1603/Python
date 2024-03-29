class vectors:

    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1=""
        str1+=f"{self.vec[0]}i + {self.vec[1]}j +{self.vec[2]}k"
        return str1
        
v1=vectors([7,8,10])
print(v1)