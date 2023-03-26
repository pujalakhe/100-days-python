stu_scores=input("enter scores of diff students:\n ").split()
for n in range(0,len(stu_scores)):
    stu_scores[n]=int(stu_scores[n])
print(stu_scores)
#simply using max or min function
# print(max(stu_score)+" is the highest score")
# print(min(stu_score)+" is the lowest score")
#without defined function

highest_score=0
for score in stu_scores:
    if score>highest_score:
        highest_score=score
print(f"the highest score among entered scores is {highest_score}")
