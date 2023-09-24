class Number:
    def sum(self):
        return self.a + self.b
num= Number()
num.a=500
num.b=600
s=num.sum()
print(s)

#static method
class Employee:
    @staticmethod
    def greet():
        print("Good Afternoon!!")
harry=Employee()
harry.greet()