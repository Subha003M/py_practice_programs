row=6
for i in range (row):
    for j in range(row):
        if (i==0 or i==5) or (j==0 or j==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()