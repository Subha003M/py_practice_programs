class emp():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(emp):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print("name",self.name,"\n","\nsalary",self.salary,"\ndept",self.dept)
e1=manager("subha","60000","developer")
e1.display()