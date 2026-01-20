y=[]
x=[1,2,3,4,5,6,5,3,2]
for i in range(0,len(x)):
     for j in range(x[i]+1,len(x)):
          if(x[i]==x[j]):
             if(x[i]not in y):
                 y.append(x[i])
for  k in range(0,len(y)):
    x.remove(y[k])
x.sort()
print(x)   