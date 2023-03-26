import random
import os
def deal_card():
    '''return random card from the deck'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return(card)

def calc_scores(cards):#cards is an input
    #checking for blackjack
    if sum(cards)==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score,comp_score):
    if user_score==comp_score:
        return "both have same score!!draw!!"
    elif comp_score==0:
        return "Opponent  win with a blackjack"
    elif user_score==0:
        return "you win with a black jack"
    elif user_score>21:
        return "you went over 21!!game end!!you loose"
    elif comp_score>21:
        return "opponent went over 21!! you win!!"
    elif user_score>comp_score:
        return "you win"
    else:
        return "you loose"

def play():   
    user_cards=[]
    comp_cards=[]
    is_gameover=False
        
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    #this while loop is for user
    while not is_gameover:
        user_score=calc_scores(user_cards)
        comp_score=calc_scores(comp_cards)
        print(f"Your cards:{user_cards},Current score:{user_score}")
        print(f"Computer card:{comp_cards[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
            is_gameover=True
        else:
            user_choice=input("type 'y' to pick another card or 'n' to pass:")
            if user_choice=="y":
                user_cards.append(deal_card())
            else:
                is_gameover=True
    #print(f"your final cards:{user_cards},your final score:{user_score},")
    print("your final cards:",user_cards ,","  "your final score:",user_score)
    #this while loop is for computer
    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_card())
        comp_score=calc_scores(comp_cards)
    print(f"computer final card:{comp_cards},final score:{comp_score}")
    print(compare(user_score,comp_score))
    
while input("type 'yes' to play the game or 'no' to exit:")=="yes":
    os.system('cls')
    play()


    
    
    
    