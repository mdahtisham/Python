class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(self.company, self.name, self.product)

coder = Programmer("coder", "skype")
prog = Programmer("prog", "Github")
coder.getInfo()
prog.getInfo()
