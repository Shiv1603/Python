class Employee:
    salary=5000
    increment=1.5

    @property
    def totalSalary(self):
        return self.salary*self.increment
        
    @totalSalary.setter
    def totalSalary(self,inc):
        self.increment=inc/self.salary

e=Employee()
print(e.totalSalary)

e.totalSalary=7500
print(e.increment)