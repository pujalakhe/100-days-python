print("welcome to pizza dilevry!!")
size=input("what size of pizza do you want? s/m/l\n")
pepe=input("do you want to add peperoni? y/n\n")
cheese=input("want an extra cheese?y/n\n")
bill=0;
if size=="s":
    bill+=15
    print(f"your bill for small pizza was {bill}")
elif size=="m":
    bill+=20
    print(f"your bill for medium pizza was {bill}")
else:
    bill+=25
    print(f"your bill for large pizza was {bill}")
    
if pepe=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
        
if cheese=="y":
    bill+=1
    
    
print(f"your total bill will be {bill}")
print("thank you!! visit again")