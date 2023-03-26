import random
random_integer=random.randint(1,10)#randint keyword is used  
print(random_integer)

random_float=random.random()
print(random_float)

#float umber between 0 to 5 ie 0.0000 to 4.99999
random_floats=random.random()*5
print(random_floats)

love_score=random.randint(1,100)
print(f"your love score is {love_score}%")