# First program is nested loop print multiply table

a =int (input("ENTER THE NUMBER ="))

for j in range (a,a+1):
    for k in range (1,11):
     print (j*k, end=" ")
    print("\n")

# second task is print row coloum 
b= int (input("ENTER THE NUMBER ="))
c= int (input("ENTER THE NUMBER ="))

row=b
columns =c

print ("rectangle STAR pattern")

for i in range (row):
 j=0
while (j< columns):
 print("*",end = " ")
 j=j+1
 i=i+1
 print("")
