# multiple Inheritence


class Employee:
    company = "Visa"
    eCode = 120

class Freelencer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelencer):
    name = "coder"


p = Programmer()
p.upgradeLevel()
print(p.level)

p.upgradeLevel()
print(p.level)