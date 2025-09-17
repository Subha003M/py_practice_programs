#tables
for i in range(1,11):
    print(i,"x 2 =",i*2)
    
#print number and get user input
a=int(input("enter number"))
b=int(input("enter number"))
for i in range(a+1,b):
    print(i)
    
#print even numbers
for i in range(a,b):
    if(i%2==0):
        print(i)
        
#count number
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
        print(i)
print("count=",count)

#sum
sum=0
for i in range(1,5):
    sum=sum+i
print(sum)