#Task1
print("Task1")
a=int(input("Enter value 1:"))
b=int(input("Enter value 2:"))
if(a>b):
    print("A is Greater Than B")
elif(a==b):
    print("Both are equal")
else:
    print("B is Greater than A")
#Task2
print("Task2")
a=input("Enter String 1")
b=input("Enter string 2")
if(a==b):
    print("Both String are same:")
    print(a)
    print(b)
else:
    print("Both string are different")
    print(a)
    print(b)
#Task3
print("Task3")
bot=input("Enter your Name/Contact/Address/Email like yyour choice :")
if(bot=="Name"):
    name=input("Enter your name:")
    print("Hey",name)
if(bot=="Mobile"):
    cont=input("Enter your contact number:")
    print("Your number is saved")
elif(bot=="Email"):
    email=input("Enter your email-id:")
    print("Your email-id is saved ")
elif(bot=="Addres"):
    addr=input("Enter your addres:")
    print("Your addres is saved")