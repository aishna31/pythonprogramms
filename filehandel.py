<<<<<<< HEAD
g=open("filepractise.txt","r")
a=g.read()
g.close()
a=a[1:18]
a=a.split(",")
b=[]
for i in range(0,len(a)):
      for j in range(i+1,len(a)):
         if(a[i]==a[j]):
           b.append(a[j])
c="".join(map(str,b))       
f=open("filepractise.txt","a")
f.write(c)
=======
a=[1,2,3,4,5,6,4,3,2]
b=[]
for i in range(0,len(a)):
  for j in range(i+1,len(a)):
         if(a[i]==a[j]):
          b.append(a[j])
c=" ".join(map(str,b))
f=open("filepractise.txt","a")
f.write(c+" ""these values are repeated in list")
>>>>>>> 3dffd07cfde143da69f20387972a923981707b44
f.close()