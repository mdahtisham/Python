class Employee:
    company = "Google"

cod = Employee()
coder = Employee()
print(cod.company)
print(coder.company)
Employee.company = "YouTube"
print(cod.company)
print(coder.company)