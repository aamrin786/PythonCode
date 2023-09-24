class Employee:
    company = "Bharat Gas"
    salary = 7000
    salaryBonous = 500

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonous
e = Employee()
print(e.totalSalary)

#             *********setter method***********
class Employee:
    company = "Bharat Gas"
    salary = 7000
    salaryBonous = 500

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonous

    @totalSalary.setter                 #setter method
    def totalSalary(self,val):
        self.salaryBonous = (-1)*(val-self.salary)

e = Employee()
print(e.totalSalary)
e.totalSalary = 5000
print(e.salary)
print(e.salaryBonous)

