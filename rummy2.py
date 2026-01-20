import random

# read balance from file
f = open("rummyfile.txt", "r")
a = f.read()
f.close()

accountbalance = int(a.split("=", 1)[1])
print("current balance in your account is", accountbalance)

betamount = int(input("please enter your bet amount! "))

def check_balance(accountbalance, betamount):
    if betamount > accountbalance:
        print("you dont have enough balance in your account")
        return False
    else:
        print("you are ready to bet now!!")
        return True

if check_balance(accountbalance, betamount):

    betnumber = float(input("please enter the number you want to bet on (1–10)! "))

    def play_game(accountbalance, betamount, betnumber):
        randomnumber = round(random.uniform(1, 10), 2)
        print("random number is:", randomnumber)

        if randomnumber > betnumber:
            print("you WON!")
            amountwon = betamount * 2
            updatedbalance = accountbalance + amountwon
            print("amount you won is", amountwon, "rupees")
        else:
            print("you LOSS! Better Luck Next Time")
            updatedbalance = accountbalance - betamount
            print("you lost", betamount, "rupees")

        print("current balance is", updatedbalance)
        return updatedbalance

    # ✅ STORE returned value
    updatedbalance = play_game(accountbalance, betamount, betnumber)

    # update file
    s = open("rummyfile.txt", "w")
    s.write("amount=" + str(updatedbalance))
    s.close()