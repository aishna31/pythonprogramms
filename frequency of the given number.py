
x=input("enter the number of which you have to find frequency")

frequency_2=0
for i in x:
    if int(i) ==2:
        frequency_2+=1
frequency_3=0
for j in x:
    if int(j)==3:
        frequency_3+=1
frequency_4=0        
for k in x:
    if int(k)==4:
        frequency_4+=1
print(frequency_2,frequency_3,frequency_4)        
