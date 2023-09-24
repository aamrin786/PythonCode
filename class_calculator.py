class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"the square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"the cube of {self.num} is {self.num**3}")
    def squareRoot(self):
        print(f"the square root of {self.num} is {self.num**0.5}")
    
    # greet user using "static method"
    @staticmethod
    def greet():
        print("****** Hey there welcome!!! ******")
        
number= Calculator(9)
number.greet()
number.square()
number.cube()
number.squareRoot()