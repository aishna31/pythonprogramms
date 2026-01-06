a=[1,2,3,4,5,6,4,3,2]
b=[]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
         if(a[i]==a[j]):
          b.append(a[j])
c=" ".join(map(str,b))
f=open("filepractise.txt","a")
f.write(c+" ""these values are repeated in list")
f.close()