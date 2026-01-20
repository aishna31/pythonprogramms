x=[
    {"a" : 1 },
    {"b" : 2 },
    {"c" : 3 },
    {"d" : 4 },
    {"e" : 5 },
    {"f" : 6 },
]
y=[]
tot=0
for i in range(0,len(x)):
    a=(list(x[i].values())[0])
    y.append(a)
    tot+=a
if tot in y:
        print("yes",x[i])
else:
        print("no it is not present")    
