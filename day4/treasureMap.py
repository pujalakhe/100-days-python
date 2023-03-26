# 🚨 Don't change the code below 👇
from tkinter import HORIZONTAL


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal=int(position[0])
vertical=int(position[1])
map[vertical-1][horizontal-1]="T"
print(f"{row1}\n{row2}\n{row3}")