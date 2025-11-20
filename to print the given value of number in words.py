
x=input("enter a number")
x=int(x)
ones="", "one", "two" , "three" , "four", "five", "six","seven","eight","nine"
tens="","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"
result=""
if x>=100:
    result=result+ones[x//100]+" hundred "
x=x%100
if x>=20:
    result=result+tens[x//10]+" "
x=x%10
if x>0:
    result=result+ones[x]
print(result)    

        