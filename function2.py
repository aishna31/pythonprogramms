
y=[]
x=[1,2,3,4,4,5,3,1]


def my_function(x):
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if(x[i]==x[j]):
                y.append(x[i])
    print(y)
a=6
b=8
my_function(x) 





z=[1,2,3,4,4,5,3,1]
my_function(z) 
