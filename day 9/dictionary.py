programming_dictonary={
   "variable": "A variable is a container that holds a single number, word, or other information that you can use throughout a program. A variable is like a chest you can fill with different values. You name the chests so you can find them later. Variables have three parts: type, name, and value.",
   "while loops":" While loops are set up just like if statements. They check for a condition and run the code in them until the condition is no longer true. A while loop will run forever (until the condition is false.",
}
for key in programming_dictonary:
    print(key)#key words are printed
    print(programming_dictonary[key])

#creating an empty dictionary
# empty_dictionary={}
# #wiping an entire  dictionary
# programming_dictonary={}
# print(programming_dictonary)

#edit an item in dictionary
# programming_dictonary["variable"]="A variable is never constant."
# print(programming_dictonary)

#adding item to dictionary
programming_dictonary["loop"]="loop helps to loop through the items"
print(programming_dictonary)