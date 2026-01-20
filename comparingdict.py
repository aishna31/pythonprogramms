x=[
    {"a" : 1 },
    {"b" : 2 },
    {"c" : 3 },
    {"d" : 4 },
    {"e" : 5 },
    {"f" : 6 },
]
y=[
    {"g": 7},
    {"h":8 },
    {"i":21},
]
z=[]
a=[]
sum=0
total=0
for i in range(0,len(x)):
    b=(list(x[i].values())[0])
    z.append(b)
    sum+=b
print("the sum is",sum)
if sum in z:
    print("yes it is there in first list",x[i])
else:
    print("no it is not there in first list")        
for j in range(0,len(y)):
    c=(list(y[j].values())[0])
    a.append(c)
    total+=c
if sum in a:
    print("yes it is present  in second list",y[j])
else:
    print("no it is not present")        