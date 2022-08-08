#A normal year has 365 days, leap years have 366, with an extra day in February.
##This is how you work out whether if a particular year is a leap year.
#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400
#e.g. The year 2000:
#2000 ÷ 4 = 500 (Leap)
#2000 ÷ 100 = 20 (Not Leap)
#2000 ÷ 400 = 5 (Leap!)
#So the year 2000 is a leap year.
#But the year 2100 is not a leap year because:
#2100 ÷ 4 = 525 (Leap)
#2100 ÷ 100 = 21 (Not Leap)
#2100 ÷ 400 = 5.25 (Not Leap)


yr=int(input("enter a year:"))
if yr%4==0:
    if yr%100==0:#if yr%4=0 is true
        if yr%400==0:#if yr%10=0 is true
             print(f"{yr} is a leap year")
        else:
            print(f"{yr} is not a leap year")
    else:
        print(f"{yr} a leap year")
else:
    print( print(f"{yr}  is not a leap year"))

