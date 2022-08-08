print("welcome to amusment park")
height=int(input("what is ur height:"))
bill=0
if height>=130:
    print("you are qualified to ride the rides!!")
    age=int(input("Enter you age:"))
    if age<=12:
        bill=150
        print(" childen ticket rs.150")
    elif age <=18:
        bill=200
        print(" youth ticket rs.200")
    else:
        bill=300
        print(" adult ticket rs.300")
    photo=input("do you want photos to be taken??(y/n)\n")
    if photo=="y":
        bill=bill+50
        print(f'your total bill will be rs.{bill}')
    else:
        print(f'your total amt will be {bill}')
else:
    print("Sorry!!you can't takes the rides.")