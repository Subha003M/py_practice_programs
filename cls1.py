class student:
    def __init__(self):
        self.name="subha"
        self.regno="098"
    def display(self):
        print("name",self.name)
        print("reg",self.regno)
s1=student()
s1.display() 
s2=student()
s2.name="sathya"
s2.regno="099"
s2.display()