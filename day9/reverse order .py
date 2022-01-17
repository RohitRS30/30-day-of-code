#task 1 print 100 in reverse order
list1 = [10, 20, 30, 40,50,60,70,80,90,100]
for num in reversed(list1):
    print(num)

#taSK 2 PRINT prime number
even = [1,2,4,6,9,10,12,14,16,18,20,22,24,26,28,30]
prime = [i + 1 for i in even ]
print(prime)

#task 3 series upto n terms
n= int(input("enter the number N ="))
fact=1
sum = 0
for a in range (1,n+1):
    fact =a
    sum = sum +a/fact

    print("sum is ",sum)