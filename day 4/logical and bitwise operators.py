#  first task is bitwise oprators

a =int (input("enter the number is ="))
b= int (input("enter the number is ="))                
c = 0

#(a)  & Binary AND
c = a & b;        
print ("& Binary AND Value of c is ", c)

#(b) | Binary OR
c = a | b;        
print ("| Binary OR Value of c is ", c)

#(c) ^ Binary XOR
c = a ^ b;        
print ("^ Binary XOR - Value of c is ", c)

#(d) ~ Binary Ones Complement
c = ~a;          
print ("~ Binary Ones Complement - Value of c is ", c)

#(e) << Binary Left Shift
c = a << 2;      
print ("<< Binary Left Shift - Value of c is ", c )

#(f) >> Binary Right Shift
c = a >> 2;      
print (">> Binary Right Shift - Value of c is ", c)

# second task is logical oprators

x = int (input("enter the number is =")) 

#(a) and Logical AND

print(x > 1 and x < 100) 

#(b)  or Logical OR

print(x > 1 or x < 100)

#(c) not (Logical not)

print(not(x > 1 and x < 100))




