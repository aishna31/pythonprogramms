x = [
    { "a":1 },
    { "b":2 },
    { "c":3 },
    { "d":4 },
    { "e":5 },
    { "f":6 } 
]

y = ['a', 'b', 'c', 'd', 'e', 'f']
sum=0
arr = []
for i in range(0,len(x)):
     a=(x[i][y[i]])
     sum+=a
     arr.append({"a" : list(x[i].values())[0]})
print(arr)
print(sum)