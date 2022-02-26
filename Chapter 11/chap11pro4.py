# Multilevel Inheritence


class Person:
    country = "India"

    def takeBreath(self):
        print("I am Breathing")


class Employee(Person):
    company = "Honda"

    def getsalary(self):
        print(self.salary)


    def takeBreath(self):
        print("I am an Employee")


class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print("no salary for programmer")

p = Person()
p.takeBreath()
e = Employee()
pr = Programmer()