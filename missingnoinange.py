
y=[]
x=[1,3,5,6,8,10]
for i in range(0,len(x)):
    if(x[i]+1!=x[1]):
        y.append(x[i]+1)
c=(x+y)
c.sort()
list(c)
for j in range(0,len(y)):
    for k in range(0,len(x)):
        if(y[j]==x[k]):
            c.remove(y[j])
print(c)            