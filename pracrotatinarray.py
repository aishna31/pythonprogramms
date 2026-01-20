x=[12,13,14,16,12,15,17,18,17,16,14]
y=[]
z=[]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if (x[i]==x[j]):
            y.append(x[j])
print(y)            