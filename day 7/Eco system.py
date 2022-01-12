print("Welcome PRO MART")
print("The Great Deal Festival of Sakranti ")
print("Product-IPhone13pro max \n Price-1,59,900 \n To buy this type 1" )
print("Product- Iphone13pro  \n Price-1,19,900\n To buy this type 2")
print("Product- Iphone13 \n Price-79,900\n To buy this type 3")
print("Product-Iphone13 mini \n Price-69,900\n To buy this type 4")
print("Product-AppleIpad pro \n price-1,10,900\n  To buy this product type 5")
a=int(input("Type your Product number:"))
if(a==1):
    print("Thanks For Selecting IPhone13pro max ")
    print("You have coupon code-(PRO40)")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="PRO40"):
        pay=1,59,900/40*100
        print(f"You win 40% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==2):
    print("Thanks For Selecting Iphone13pro")
    print("You have coupon code-(PRO30)")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="PRO30"):
        amount= 1,19,900
        Discount= amount*30/100
        print("You Win 5% discount")
        print("Net payable amount is:",amount-Discount)
    else:
        print("You have Enter invalid coupon code")
if(a==3):
    print("Thanks For Selecting Iphone13  ")
    print("You have coupon code-(PRO20)")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="PRO20"):
        pay=79,900*(20/100)
        print()
        print(f"You Win 20% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==4):
    print("Thanks For Selecting Iphone13 mini ")
    print("You have coupon code-(PRO15)")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="PRO15"):
        pay=69,900*(10/100)
        print(f"You Win 15% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")

if(a==5):
    print("Thanks For Selecting AppleIpad pro")
    print("You have coupon code-(PRO40)")
    d=input("Type your coupon code to get some disconnt:")
    if(d=="PRO40"):
        pay=1,10,900*40/100
        print(f"You Win 40% discount")
        print(f"Net payable amount is:{pay}")
    else:
        print("You have Enter invalid coupon code")