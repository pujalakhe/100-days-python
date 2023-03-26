import random
user_action=input("Choose any of the following\nrock\npaper\nscissor:\n")
possible_actions=["rock","scissor","paper"]
computer_action=random.choice(possible_actions)
print(f"User choice={user_action}\nComputer choice={computer_action}")
if user_action==computer_action:
    print("Both chooses same,So it a tie")
elif user_action=="rock":
    if computer_action=="scissor":
        print("rock smashes the sissor!!!you win")
    else:
        print("paper cover the rock!!you loose")
elif user_action=="scissor":
    if computer_action=="paper":
        print("scissor cuts the paper!!you win")
    else:
        print("rock smashes the scissor!!!you loose")
elif user_action=="paper":
    if computer_action=="rock":
        print("paper cover the rock!!you win")
    else:
        print("scissor cuts the paper!!you loose")
else:
    print("invalid input by user!!!")
        
                
            