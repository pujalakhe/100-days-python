stu_scores={
    "Puza":88,
    "Jisoo":95,
    "Sunghoon":92,
    "Niki":75,
}
#creating empty dictionary
stu_grades={}

for student in stu_scores:
    score=stu_scores[student]
    if score>90:
        stu_grades[student]="Outstanding"
    elif score>80:
        stu_grades[student]="Exceed Expection"
    elif score>70:
        stu_grades[student]="Acceptable"
    else:
        stu_grades[student]="Fail!!work hard"
print(stu_grades)
