x=[15,16,18,21,15,21,15]
y=[]
for i in range(0, len(x)):
    frequency=1
    if(x[i] not in y):
        y.append(x[i])
        for j in range(i+1, len(x)):
                if(x[i] == x[j]):
                        frequency += 1                        
    if(frequency > 1):
        print(x[i], "Frequency number =",frequency)