class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(self.name)
        print(self.train)

Application = RailwayForm()
Application.name = "coder"
Application.train = "express"
Application.printData()