print("!!!!!!!!!!!welcome to split bill calulator!!!!!!!!!!!")
bill=float(input("Enter the total amount of bill:"))
tip=int(input("what percentage tip would you like to split:12,15,20: "))
people=int(input("Number of people to split bill:"))
#in case of nepal where tip not required
#split=int(bill)/int(people);
#print(split)
totalbill=tip/100*bill+bill
total=totalbill/people
print("each person should pay rs.",total)