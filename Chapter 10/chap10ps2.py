class Calculator:
    def __init__(self, num):
        self.number = num

    def squar(self):
        print(self.number, self.number **2)

    def  squareRoot(self):
        print(self.number, self.number **0.5)

    def cube(self):
        print(self.number, self.number **3)

a = Calculator(5)
a.squar()
a.squareRoot()
a.cube()