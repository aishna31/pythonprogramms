n=int(input("enter the number of times you need to rotate the value"))
x=[1,2,3,4,5,6,7,8,9,10]
y=[]
z=[]
for j in range(len(x)-n+1,len(x)+1):
    y.append(j)
for i in range(0,len(x)-n):
    z.append(x[i])
b=(y+z) 
print(b)
   
