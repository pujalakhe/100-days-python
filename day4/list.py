import random
#split method
names=input("give me different individual name spereated by comma \n")
names_split=names.split(",")

#actual code
len(names_split)
name_no=len(names_split)

random_name=random.randint(0,name_no-1)
person_who_will_buy=names_split[random_name]
#person_who_will_buy=random.choice(names_split)
print(person_who_will_buy + " gonnay pay")
