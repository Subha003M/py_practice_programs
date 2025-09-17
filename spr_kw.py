class a():
    def __init__(self):
        print("a")
    def display(self):
        print("class A")
class b(a):
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("class B")
class c(b,a):
    def __init__(self):
        super().__init__()
        print("c")
        
    def display(self):
        print("class C")
obj=c()