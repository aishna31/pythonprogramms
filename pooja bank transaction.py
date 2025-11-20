
balance=10000
amt=int(input("enter the amount "))
if(amt>balance):
    print("you dont have enough balance in your account")
elif(amt%5==0):
    a=amt+0.50
    b=balance-a
    print("balance present =",b)