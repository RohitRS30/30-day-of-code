# first program compound interest 
print ("caculate compound interest ")
p = int(input("enter principal value = "))
t = int(input("enter time value = "))
r = float(input("enter rate value = "))
a = p*(pow((1+r/100),t))
print ("amount = ",a)
ci = a-p
print("compount interest  :",ci)

# second program  calculate persentage
print("caculate persentage")
x = float(input("enter your marks  = ")) 
per = 100
y = float(input("enter total marks  = ")) 
z = x*per/y
print ("your persentage = ",z) 

# third print only first middile and last value string

m = "Mr"
n = "Hope"
print(m[0:2])
print(n[0:1])
print(n[0:3])



