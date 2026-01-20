
x=input("enter a three digit number")
total=0
for i in range(0,len(x)):
    num=int(x[i])
    cube=num*num*num
    total+=cube   
if(total == int(x)):
    print("yes ")
else:
    print("no")    