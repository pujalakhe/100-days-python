# get the height
height=float(input("Enter ur height in m:"))
#get the weight
weight=float(input("Enter ur weight in kg:"))
#claculate the BIM but before bim calculate convet them into correct/needed datatypes as they are previously in string types
bim = round((weight / height**height),2)
#or bim = int(weight) / float(height)**2
#also convert the result of BIM into integer type for whole number ans
#print("your BIM is",(bim))
if bim<18:
    print(f"your BMI is {bim},you are underweight")
elif bim<25:
    print(f"your BMI is {bim},you have a normal weight")
elif bim<30:
    print(f"your BMI is {bim},you are overweight")
elif bim<35:
    print(f"your BMI is {bim},you are obese")
else:
    print(f"your BMI is {bim},you are clinically obesed")