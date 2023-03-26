# import random
# ## characters to generate password from
# characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# print("welcome to PUZA'Z password generator!!!!\nYOROSHEKUN")
# n_letters=int(input("how many letters would you like in your password\n"))
# n_symbols=int(input("how many symbols would you like in your password\n"))
# n_digits=int(input("how many digits would you like in your password\n"))
# #easy way
# password=""
# for letter in range(1,n_letters+1):
#     random.choice(characters)
# print(characters)


import string
import random


## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))
	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	## converting the list to string
	## printing the list
	print("".join(password))



## invoking the function
generate_random_password()