a=int(input("enter a number"))
b=int(input("enter a number"))
def add():
    
    print("addition=",a+b)
def sub():
    print("subtraction=",a-b)

def mul():
    print("multiplication=",a*b)
def div():
    try:
        print("Division =", a / b)
    except ZeroDivisionError as e:
        print("Error:", e)
        
add()
sub()
mul()
div()        
