#display the art
from operator import truediv
from pickle import FALSE, TRUE
import random
import os
from art import logo
from gamedata import data

#formate the acc data into printable form
def format(account):
    account_name=account['name']
    account_desc=account['description']
    account_country=account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_ans(guess,a_followers,b_followers):
    """use if statement to check if use is correct"""  
    if a_followers>b_followers:
        return guess=="a"
    else:
        return guess=="b"
    
print (logo)
score=0
#make the game repeatable
game_continue=True
account_b=random.choice(data)
#generate random acc frm game data
while  game_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"compare A:{format(account_a)}")
    print("            vs            ")
    print(f"Against B:{format(account_b)}")

    #taking user guess
    guess=input("Who has more followers?Type 'A' or 'B':").lower()

    #checking user input
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_ans(guess,a_follower_count,b_follower_count)
    os.system('cls')
    print(logo)
    #score keeping and give user the feedback
    if is_correct:
        score+=1
        print(f"You are right!!Current score={score}")
    else:
        print(f"wrng ans!!Your final score is {score}")
        game_continue=False