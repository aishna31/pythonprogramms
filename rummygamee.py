import random
f=open("rummyfile.txt","r")
a=f.read()
accountbalance=int(a.split ("=",1)[1])
print("current balance in your account is",accountbalance)
betamount=int(input("please enter your bet amount!"))
def myfunction(accountbalance,betamount):
    if betamount>accountbalance:
        print("you dont have enogh balance in your account")
    else:
        print("you are ready to bet now!!")   
myfunction(accountbalance,betamount)        
betnumber=float(input("please enter the number you want to bet on!"))  
#function to start game , generate random number 
def yourfunction(accountbalance,betamount,betnumber):
    randomnumber=round(random.uniform(1,10),2)
    print("your number is!",randomnumber)
    #you won or you loss
    if(randomnumber>betnumber):
        print("you WON!")
        amountwon=betamount*2
        print("amount you won is",amountwon,"ruppes")
        updatedbalance=accountbalance+amountwon
        print("the current balance in your account is",updatedbalance)
        return updatedbalance
    else:
        print("you LOSS! Better Luck Next Time")
        updatedbalance=accountbalance-betamount
        print("you loss",betamount,"ruppes") 
        print("the current balance in your account is",updatedbalance)
        return updatedbalance
yourfunction(accountbalance,betamount,betnumber)    
#function to update the values in the amount file 
def ourfunction(accountbalance,updatedbalance):
    s=open("rummyfile.txt","w")
    s.write("amount=" + str(updatedbalance))
    s.close()  
ourfunction(accountbalance,updatedbalance)    
