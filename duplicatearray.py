<<<<<<< HEAD

x=[1,22,33,44,5,44,33,21,22,71,71,1]
y=[]
z=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
            y.append(x[i])
    if(x[i] not in y):
            z.append(x[i])
print(z)                

            
   
=======

x=[1,22,33,44,5,44,33,21,22,71,71,1]
y=[]
z=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
            y.append(x[i])
    if(x[i] not in y):
            z.append(x[i])
print(z)                

            
   
>>>>>>> 3dffd07cfde143da69f20387972a923981707b44
