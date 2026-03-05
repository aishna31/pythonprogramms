# to get the pin 
userpin=input("pls enter your pin")
a=open("atmpassword.txt","r")
b=a.read()
a.close()
pin=b.split("=",1)[1]
# to check wether pin is correct or not
if (userpin==pin):
    print("what task you have to perform?")
    task=input("1.check balance            2.deposite money           3.withdraw money")
    if (task=="check balance"):
        c=open("atm.txt","r")
        checkbalance=c.read()
        c.close()
        print(checkbalance)
    elif(task=="checkbalance"):
        d=open("atm.txt","r")
        checkbalance=d.read()
        d.close()
        print(checkbalance)
    elif(task=="1"):
        e=open("atm.txt","r")
        checkbalance=e.read()
        e.close()
        print(checkbalance)
    elif(task=="2"):
        depositeamount=int(input("please enter the amount you need to deposite"))
        f=open("atm.txt","r")
        accbalance=f.read()
        f.close()
        accbalance= int(accbalance.split("=")[1])
        newdepositebalance=accbalance+depositeamount
        print(depositeamount,"is successfully added to you account")
        print("the current balance in your acc after updation is ",newdepositebalance)
    elif(task=="depositemoney"):
        depositeamount=int(input("please enter the amount you need to deposite"))
        f=open("atm.txt","r")
        accbalance=f.read()
        f.close()
        accbalance= int(accbalance.split("=")[1])
        newdepositebalance=accbalance+depositeamount
        print(depositeamount,"is successfully added to you account")
        print("the current balance in your acc after updation is ",newdepositebalance)
    elif(task=="deposite money"):
            depositeamount=int(input("please enter the amount you need to deposite"))
            f=open("atm.txt","r")
            accbalance=f.read()
            f.close()
            accbalance= int(accbalance.split("=")[1])
            newdepositebalance=accbalance+depositeamount
            print(depositeamount,"is successfully added to you account")
            print("the  current balance in your acc after updation is ",newdepositebalance)

else:
    print("incorrect pin")    
