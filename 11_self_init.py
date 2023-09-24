class Employee:
    company="Google"
    def getSalary(self):       
        print("Salary is 100k")
harry = Employee() #made a new object of employee class
harry.getSalary() # == Employee.getSalary(harry)

#  OR
class Employee:
    company="Google"
    def getSalary(self,signature):       
        print(f"Salary for this employee in {self.company} is {self.salary}\n{signature}")

        # *****************************
     #staticmethod   
    @staticmethod
    def greet():
      print("Good Afternoon!! Sir")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!!")
harry.greet()
#                *****************************************

# __init__Constructor
class Employee:
    company='Google'
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")
    def getDetails(self):
        print(f"The name of the employee is:{self.name}")
        print(f"The salary of the employee is:{self.salary}")
        print(f"The subunit of the employee is:{self.subunit}")
harry = Employee("Aamrin",100000,"Camera")
harry.getDetails()