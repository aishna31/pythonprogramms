f=open("password.txt","r")
password=f.read()
f.close
password=password.split("=",1)[1]
print("to access your file you have to enter a password!")
userpassword=input("enter a password")
if(userpassword==password):
    print("your password was correct ,here is your data!")
    p=open("datafile.txt","r")
    data=p.read()
    print(data)
else:
    print("your password is incorrect")
    userpassword=input("enter your password again!!")
    if(userpassword==password):
         print("your password was correct ,here is your data!")
         p=open("datafile.txt","r")
         data=p.read()
         print(data)
    else:
        print("your password was incorrect")
        userpassword=input("enter your password again!")
        if(userpassword==password):
         print("your password was correct ,here is your data!")
         p=open("datafile.txt","r")
         data=p.read()
         print(data)
    print("OOPS! your limit is over  bye bye")     


