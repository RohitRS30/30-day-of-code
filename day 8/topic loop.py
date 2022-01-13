# task 1 is display the number -10 to -1 using for loop
for i in range (-10,0):
    print(i,end="")
    i=i+1
    print (" ")


     
 # task 2 is display the number in a form of martrix
r= int(input("enter the row = ")) 
s =int(input("enter the coloumn = "))  
matrix =[]
for i in range (r):
    m=[]
    m.append(i)
for j in range (s):
    j=int(input("enter number of pocket "+str(i)+" "+str(j)+" "))
matrix.append(m)

for i in range (r):
    for j in range (s):
        print(matrix [i][j],end=" ")
print()
        
#task 3 isprint a one time b wo time..

row= 1 
for i in range(0,5):
    print(chr(65+i)*(i+1))
    i=i+1