class Person:         #parent
    country = "India"
    def hobby(self):
        print("Hobby is gardenning")

class Employee(Person):     #Child 1
    company = "Google"

    def salary(self):
        print(f"Salary is {self.salary}")

    def hobby(self):
        super().hobby()     #super() function
        print("Hoby is gardenning and drawing")

class Programmer(Employee):     #Child 2
    company="Fiverr"

    def salary(self):
        print(f"No salary to programmers")

    def hobby(self):
        super().hobby()     #super() function
        print("Hobby is gardenning and driving")

p=Person()
e=Employee()
pr=Programmer()
print(e.company)
# print(p.company) error
e.hobby()
pr.hobby()