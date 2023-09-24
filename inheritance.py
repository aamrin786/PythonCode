#Multiple Inheritance
class Employee:       #Parent 1
    company="Visa"

class Freelancer:      #Parent 2
    company = "Fiverr"
    level = 3
    def levelUP(self):
        self.level = self.level +1
    
class Programmer(Employee,Freelancer):
    name = "Rohit"

p=Programmer()
print(p.company)
print(p.level)
p.levelUP()
print(p.level)

#Multilavel Inheritance
class Person:         #parent
    country = "India"
    def hobby(self):
        print("Hobby is gardenning")

class Employee(Person):     #Child 1
    company = "Google"

    def salary(self):
        print(f"Salary is {self.salary}")

    def hobby(self):
        print("Hoby is gardenning and drawing")

class Programmer(Employee):     #Child 2
    company="Fiverr"

    def salary(self):
        print(f"No salary to programmers")

p=Person()
e=Employee()
pr=Programmer()
print(e.company)
# print(p.company) error
pr.hobby()
e.hobby()