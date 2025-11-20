
x=[1,2,3,4,5]
for i in range(0,len(x)):
    if (x[i]>x[1]):
        temp=x[i]
        if (x[i]>x[2]):
            temp=x[i]
            if(x[i]>x[3]):
                temp=x[i]
                if(x[i]>x[4]):
                    temp=x[i]
                print("the max value is new", temp )    


