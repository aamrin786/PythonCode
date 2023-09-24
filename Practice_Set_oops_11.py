class C2dVec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return (f"{self.icap}i+{self.jcap}j")
class C3dVec:
    def __init__(self,i,j,k):
        self.icap = i
        self.jcap = j
        self.kcap = k

    def __str__(self):
        return (f"{self.icap}i+{self.jcap}j+{self.kcap}k")

v2d = C2dVec(1,3)
v3d = C3dVec(1,9,7)
print(v2d)
print(v3d)

# complex numbers
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real+c.real, self.imaginary+c.imaginary)

    def __mul__(self,c):          #multiplication formula
        mulreal= self.real*c.real - self.imaginary*c.imaginary
        mulimaginary = self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulreal,mulimaginary)


    def __str__(self):
        return (f"{self.real}+{self.imaginary}i")

c1=Complex(1,4)
c2=Complex(8,5)
print(c1+c2)   
print(c1*c2)

# sum and dot product
class Vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str1 +=f" {i}a{index} +"
            index+=1
        return str1[:-1]     #if i don't use this line it will print a extra + sign at the end of the output
    def __add__(self,vec2):

        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return Vector(newlist)

    def __mul__(self,vec2):
        for i in range(len(self.vec)):
          sum=0
          sum +=(self.vec[i] * vec2.vec[i])
        return sum
    
    def __len__(self):
        return len(self.vec)
        


v1 = Vector([1,4,6])
v2 = Vector([2,5,4])
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))