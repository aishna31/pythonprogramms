# to get the input from user
username=input("what is your good name?")
print("hello!!", username,"welcome to task manager")
print("please select the task you need to perform!")
taskinput=input("1. add task           2. shechdule your day      3. view task")
if (taskinput=="1"):
    addinput=input("pls enter the task you need to add")
    fileinput="new task = " + addinput
    a=open("taskmanager.txt","a")
    a.write(fileinput)
    a.close()
elif(taskinput=="2"):
    dayinput=input("you can schedule your day here!")
    a=open("taskmanager.txt","a")
    a.write(dayinput)
    a.close()  
elif(taskinput=="3"):
    a=open("taskmanager.txt","r")
    useroutput=a.read()
    a.close()
    print(useroutput)