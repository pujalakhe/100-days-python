# get the height
height=input("Enter ur height in m:")
#get the weight
weight=input("Enter ur weight in kg:")
#claculate the BIM but before bim calculate convet them into correct/needed datatypes as they are previously in string types
bim = int(weight) / float(height)**float(height)
#or bim = int(weight) / float(height)**2
#also convert the result of BIM into integer type for whole number ans
print("your BIM is",int(bim))