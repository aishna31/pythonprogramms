import random
#reading amount balance from file
f=open("rummyfile.txt","r")
a=f.read()
f.close()
acountbalance=int(a.split("=",1)[1])
def myfunction(acountbalance,betnumber,betamount):
    randomnumber=round(random.uniform(1,10),2)
    print("your number is!",randomnumber)
    #you won or you loss
    if(randomnumber>betnumber):
        print("you WON!")
        amountwon=betamount*2
        print("amount you won is",amountwon,"ruppes")
        updatedbalance=acountbalance+amountwon
        print("the current balance in your account is",updatedbalance)
        return updatedbalance
    else:
        print("you LOSS! Better Luck Next Time")
        updatedbalance=acountbalance-betamount
        print("you loss",betamount,"ruppes") 
        print("the current balance in your account is",updatedbalance)
        return(updatedbalance)
#the game is now started 
print("welcome to the rummy game!")
print("current balance in your account is",acountbalance)
betamount=int(input("enter your bet amount"))
#checking balance
if (betamount>acountbalance):
    print("sorry you dont have enough balance in your account!! your current balance is",acountbalance)
    exit()
#actual starting    
else:
    betnumber=float(input("enter your bet number between 1.0 to 10.0"))
#generating random number
reuslt =myfunction(acountbalance,betnumber,betamount)
#update balance in the file 
updatedbalance = reuslt
s=open("rummyfile.txt","w")
s.write("amount=" + str(updatedbalance))
s.close()    
#asking if they want to play a new game 
print("DO YOU WANT TO START NEXT GAME ??")
answer=input("YES OR NO?")
if answer=="yes":
    betamount=float(input("enter your bet amount"))
    if(betamount>updatedbalance):
        print("SORRY YOU DONT HAVE ENOUGH BALANCE TO CONTINUE")
    else:
        betnumber=float(input("enter your bet number between 1.0 to 10.0"))
        myfunction(acountbalance,betnumber,betamount)
        s=open("rummyfile.txt","w")
        s.write("amount=" + str(updatedbalance))
        s.close()
else:
    print("THANKYOU FOR PLAYING ")