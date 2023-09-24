class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("Let's add")
        return self.num + num2.num

    def __truediv__(self,num2):
        print("Let's multiply")
        return self.num/num2.num

n1= Number(10)
n2= Number(4)

sum = n1 + n2
mul = n1/n2
print(sum)
print(mul)


