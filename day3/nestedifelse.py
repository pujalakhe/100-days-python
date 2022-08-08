print("welcome to amusment park")
height=int(input("what is ur height:"))
if height>=130:
    print("you are qualified to ride the rides!!")
    age=int(input("Enter you age:"))
    if age<=12:
        print("please pay rs.150")
    elif age <=18:
        print("you need to pay rs.200")
    else:
         print("play rs.300")
else:
    print("Sorry!!you can't takes the rides.")