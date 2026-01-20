y=[]
x=[1,3,5,7]
for i in range(0,len(x)-1):
    if(x[i]+1 != x[1]):
       y.append(x[i]+1)
c=(x+y)
c.sort()
print(c) 