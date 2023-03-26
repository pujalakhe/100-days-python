def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+":add,  
    "-":sub,
    "*":mul,
    "/":div,
}
import os
def calculator():
    num1=float(input("enter the first number:"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operations_symbol=input("pick an operations:\n")
        num2=float(input("enter the next number:"))
        calculation_function=operations[operations_symbol]
        ans=calculation_function(num1,num2)
        print(f'{num1} {operations_symbol} {num2} = {ans}')
        choice=input(f"type 'y' to continue calculating with {ans} or 'n' to start new calculation\n !!or e to completely turn off the calculator :")
        if choice=="y":
            num1=ans
        elif choice=="n":
            should_continue=False
            os.system('cls')
            calculator()
        else:
            should_continue=False
            print("The calculator has been turned off!!")
            
#calling the function a must line of code        
calculator()