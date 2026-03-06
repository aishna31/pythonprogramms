<<<<<<< HEAD
x=[1,2,3,4,2,5,4,3]
y=[]
z=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
           y.append(x[i])  
    if(x[i] not in y):
            z.append(x[i])
a=(z+y)
a.sort()
print(a)

           

                 
        
=======
x=[1,2,3,4,2,5,4,3]
y=[]
z=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
           y.append(x[i])  
    if(x[i] not in y):
            z.append(x[i])
a=(z+y)
a.sort()
print(a)
