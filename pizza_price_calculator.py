# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 17:20:45 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


if (size  == 'S') | (size == 's'):
    bill = 15
    if (add_pepperoni == 'Y') | (add_pepperoni == 'y'):
        bill += 2
elif (size == 'M') | (size == 'm'):
    bill = 20
elif (size == 'L') | (size == 'l'):
    bill = 25
else:
    print("Incorrect input! Please try again.")

if (add_pepperoni == 'Y') | (add_pepperoni == 'y'):
    bill += 3
    
if (extra_cheese == 'Y') | (extra_cheese == 'y'):
    bill += 1

print(f"Your final bill is: ${bill}.")