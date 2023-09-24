# 1. create a class programmer for storing information of few programs
class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name}")
        print(f"The name of the product is {self.product}")
aamrin=Programmer("Aamrin","Word")
raj=Programmer("Raj","Excel")
aamrin.getInfo()
raj.getInfo()
