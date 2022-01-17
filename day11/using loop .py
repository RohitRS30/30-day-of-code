#first reverse order
a=[2,3,4,5,6,7]
for i in range(len(a)-1,-1,-1):
    print(i,end=" ")
    print()

#seond concatenate two list
p=[1,2,3]
r=[4,5,6]
print ('list 1=',p)
print ('list 2=',r)
s = [i+j for i,j in zip(p,r)]
print ("the  concatenate lists:",s)

#third input list

t=[]
u=int(input("enter value ="))
print('enter u value')
for i in range (u):
    x=int(input())
    t.append(x)
    print('list is :',t)

#four display number 
o=[1,2,3,4,5,6,]
print("printing lists using  loop: ")
for i in range(len(o)):
    print(o[i],end="")
