word_lists=["bottle","charger","mobile","battery"]
import random
chosen_word=(random.choice(word_lists))
#print(f"the solution is {chosen_word}")
#creating empty list display
display=[]
lives=6
word_len=len(chosen_word)
for i in range(word_len):
    display+="_" 
print(display)
end_of_game=False
while not end_of_game:
    guess=input("guess a letter to complete the given word:").lower()
    #check guessed letter
    for position in range(word_len):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_gamee=True
            print("Game Over !!!you loose")
    #join all the elemnets into the string and display it 
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game=True
        print("you win")