class Calculator:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def op(self):
        print("add", self.x + self.y)
        

c = Calculator(2,4)
c.op()


