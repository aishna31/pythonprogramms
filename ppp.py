pattern="*"
for j in range(0,5):
    str=""
    for i in range(5-j, j, -1):
        str+=pattern
    print(str)       