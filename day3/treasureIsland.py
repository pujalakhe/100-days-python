print("The GREAT ERA OF PIRATES has been started\nFInd the treasure Aho!!!")
name=input("enter your name :\n")
print("let's start the treasure hunt",name)
choose=input("choose between left or right\n(left/right):")
if choose=="left":
    print("good one honey!!")
    choose1=input("Do you wanna swim or wait for the boat:(swim/wait)")
    if choose1=="wait":
        print("hello i am an  nacy\ncome with me i will take you to the treasurw island",name)
    else:
        print("GAME OVER\nyou have been eaten by a giant shark",name)
    print("you have reached an treasure island!!!\n")
    choose2=input("Choose a rood with following colour\n:(yellow\purple\green)")
    if choose2=="yellow":
        print("GAME OVER\nyou have been burned by fire",name)
    elif choose2=="purple":
        print("GAME OVER\nyou have been killed by a purple tongue monster",name)
    else:
        print("go to the end of the room and you will find a key and a treasure\nopen it and the treasure is yours!!!CONGRATULATIONS",name)
else:
    print("wrong choice\n GAME OVER" ,name + " better luck next time")