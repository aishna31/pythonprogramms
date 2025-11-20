
# x=input("enter the number")
# x=int(x)
# ones="", "one", "two" , "three" , "four", "five", "six","seven","eight","nine"
# tens="","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"
# result=""
# if x>=1000:
#     result= result+ ones[x//1000]+"thousands"
# x=x%1000
# if x>=100:
#     result=result+ ones[x//100]+ "hundreds "
# x=x%100
# if x>=20:
#     result=result+tens[x//10]
# x=x%10
# if x>0:
#     result=result+ones[x]
# print (result)
        

num = int(input("Enter a number: "))

ones = ["", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"]

result = ""

x = num

# Crore
if x >= 10000000:
    crore = x // 10000000
    if crore < 20:
        result += ones[crore] + " crore "
    else:
        result += tens[crore // 10] + " " + ones[crore % 10] + " crore "
    x %= 10000000

# Lakh
if x >= 100000:
    lakh = x // 100000
    if lakh < 20:
        result += ones[lakh] + " lakh "
    else:
        result += tens[lakh // 10] + " " + ones[lakh % 10] + " lakh "
    x %= 100000

# Thousand
if x >= 1000:
    thousand = x // 1000
    if thousand < 20:
        result += ones[thousand] + " thousand "
    else:
        result += tens[thousand // 10] + " " + ones[thousand % 10] + " thousand "
    x %= 1000

# Hundred
if x >= 100:
    result += ones[x // 100] + " hundred "
    x %= 100

# Tens & ones
if x >= 20:
    result += tens[x // 10] + " "
    x %= 10

if x > 0:
    result += ones[x]

print(result.strip())
