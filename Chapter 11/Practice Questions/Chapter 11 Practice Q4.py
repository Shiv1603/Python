class Complex:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        return self.num+num2.num
    
    def __mul__(self,num2):
        return self.num*num2.num
    
n1=Complex(4)
n2=Complex(6)
sum=n1+n2
mul=n1*n2
print(sum)
print(mul)