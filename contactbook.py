username=input("please enter your name")
print("hello",username ,"Welcome to your contacts!")
# to open and read the file
f=open("contact.txt","r")
z=(f.readlines())
f.close()
# to ask what is users need
print(username,"please select what you want to perform?")
print("1. you want to find a number?")
print("2. you want to add a number?")
print("3. you want to delete a number?")
print("pls enter the serial number of the task you need to perform ")
userinput=input()
# to find a contact
if (userinput=="1"):
    print("please enter the name of the person you need to find number")
    nameinput=input()
    for i in z:
        if nameinput in i:
          print(i)
#  to add a contact   
if(userinput=="2"):
    print("please enter the number and name you want to add ")
    print("pls enter number")
    noaddinput=input() 
    if(len(noaddinput)==10):
        print("please enter the name by which you have to save your conact")
        nameaddinput=input()
        addinput = nameaddinput + ":" + noaddinput        
        s=open("contact.txt","a")
        s.write(addinput)
        s.close()
        print("your number is succesfully added!") 
    else:
        print("INVALID NUMBER, your number should be of 10 digits")    
# to delete a contact
if(userinput=="3"):
  deleteinput = input("Enter the name you want to delete: ")

  m = open("contact.txt", "r")
  o = m.readlines()
  m.close()

  for k in o:
    if deleteinput in k:
        print("Are you sure you want to delete this contact? (yes/no)")
        yesorno = input().lower()

        if yesorno == "yes":
            o.remove(k)

            m = open("contact.txt", "w")
            m.writelines(o)
            m.close()

            print("Your contact is successfully deleted!")
        else:
            print("contact not found.")

        break