
x="1234"
first=0
last=0
for i in range(0,len(x)):
    if(i==0):
        first=x[i]
    if(i==len(x)-1):
        last=x[i]
print(first,last)   
