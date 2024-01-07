# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:45:36 2023
@author: Luvkush
"""

def calculator(number1, number2, operation):
    print("\n")
    if operation == '+':
        print("Performing Additon Operation...\nResult: ", end="")
        return number1+number2
    elif operation == '-':
        print("Performing Substraction Operation...\nResult: ", end="")
        return number1-number2
    elif operation == '*':
        print("Performing Multiplication Operation...\nResult: ", end="")
        return number1*number2
    elif operation == '/':
        print("Performing Division Operation...\nResult: ", end="")
        return round(number1/number2,2)
    else:
        return "Invalid Operation selected! Please try again!"

while(True):
    
    print("******* Welcome to Calculator *******\n")
    first_number = input("Please enter the first number: ").strip()
    second_number = input("Please enter the second number: ").strip()
    operation = input("Please input the operation symbol to perform(+,-,*,/): ")
    
    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except Exception as exception:
        print(f"\nError occured: {exception}: Please enter only numbers (with or without demicals.)")
    else:
        result = calculator(first_number, second_number, operation)
        print(result)
    
    control = input("\nDo you want to continue using calculator(Press any key to continue, q to quit calculator): ").lower()
    
    if control == 'q':
        break
    print("\n")

    
    


