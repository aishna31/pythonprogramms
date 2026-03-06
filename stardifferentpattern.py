
for i in range(0, 5):
    str = ""
    for k in range(i,5):
        str = str + " "
    for j in range(0,i+1):
        str += "* "
    print( str )