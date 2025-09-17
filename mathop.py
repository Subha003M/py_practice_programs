a=int(input("enter a"))
b=int(input("enter b"))
while True:
    op=input("add/sub//mul/div")
    if(op=="add"):
        print(a+b)
        break
    elif(op=="sub"):
        print(a-b)
        break
    elif(op=="mul"):
        print(a*b)
        break
    elif(op=="div"):
        print(a/b)
        break
    else:
        print("enter a valid operation")
