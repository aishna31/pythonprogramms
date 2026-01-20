
y=[]
x=[1,2,3,4,4,5,3,1]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]==x[j]):
            y.append(x[i])
print(y)