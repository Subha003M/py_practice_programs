for i in range(1, 8):
    for j in range(i):
        print(j + 1, end='')
    print()

for i in range (8,0,-1):
    for j in range (i):
        print("*",end="")
    print()
    
    
n=5
for i in range (1,n+1):
    spaces=n-i
    star=2*i-1
    print(""*spaces,"*"*star) 
    
n=3
for i in range(1,n+1):
    star="*"+(2*i-1)
    print(star.center(2*n-1))