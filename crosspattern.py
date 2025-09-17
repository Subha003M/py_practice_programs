row=7
  
for i in range(row):
    for j in range(row):
        if(i==j or j == row-1-i):
            print("*",end="")
        else:
            print(" ",end="")
    print()