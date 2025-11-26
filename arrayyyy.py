
a=[8,12,31,16,23,48]
b=[]
len_a=len(a)
for i in range(0,len(a)):
    inx=len_a-1-i
    c=a[inx]
    b.append(c)
print(b)    