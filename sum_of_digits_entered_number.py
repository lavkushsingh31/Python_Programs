# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:22:21 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

# This program takes input from user, and returns the sum of digits

def sum_of_digits(num):
    
    
    try:
        num = int(num)
    except:
        return "Please give a valid integer input!"
    
    print(f"\nYou have entered: {num}")
    print(f"Type: {type(num)}")

    sum = 0
    
    while(num>0):
        rem = num%10
        sum = sum + rem
        num = num//10    
    return sum

user_input = input("Enter any integer number: ")
digits_sum = sum_of_digits(user_input)
print(f"\nSum of Digits: {digits_sum}")




