#finding avg heigt of students
stud_height=input("differnt student height:\n").split()
for n in range(0,len(stud_height)):
    stud_height[n]=int(stud_height[n])
print(stud_height)
    
total_height=0
for height in stud_height:
    total_height+=height
print(total_height)

stu_no=0
for student in stud_height:
    stu_no+=1
print(stu_no)
avg=(total_height/stu_no)
print(avg)


#we can also use sum and len function for total height and finding no of students
# total_height=sum(stud_height)
# no_of_stu=len(stud_height)
# avg=total_height/no_of_stu
# print(avg)