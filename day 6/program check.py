print("Task1")
a=int(input("Enter number:"))
if(a%2==0):
    print("Number is divisible by 2")
else:
 print("Number is not divisible by 2")
    
#Task2
print("Task2")
a=str(input("Enter your name"))
b=int(input("Enter your percentage"))
if(b>90):
    print("Grade::A")
    print("outstanding ",a)
elif(b>80 and b<=90):
     print("Grade::B")
     print("Excellent ",a)
elif(b>=60 and b<=80):
    print("Grade::C")
elif(b>=50 and b<60):
    print("Grade::D")
    print("good",a)
elif(b>=33 and b<50):
    print("Grade::E")
    print("try to best",a)
else:
    
    print("You are Fail!!!")
 
