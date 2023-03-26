from random import randint
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0

def compare(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"You guess the answer'{answer}' correctly......You win")

def difficulty():
    choice=input("Choose a difficulty level\n 'easy' OR 'hard':\n")
    if choice=="easy":
        return EASY_LEVEL_TURNS 
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    print ("!!!!!!!!!!!welcome to NUMBER GUESSING GAME!!!!")
    name=input("Enter the players name:")
    print(f"{name},Guess a number between 1 to 100")
    answer=randint(1,100)
    #print(answer)

    turns=difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess=int(input("Make a guess:"))
        turns=compare(guess,answer,turns)
        if turns==0:
            print("you run out of attempts/chances to guess..\nTRY AGIAN!!")
            print(f"the correct ans was {answer}.")
            return
        elif guess!=answer:
            print("Guess again!!")
           

game()