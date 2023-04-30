# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:58:55 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

print("Welcome to the Roller Coaster")
height = float(input("Enter your height (in cms): "))
bill = 0
if height >= 120:
    print("Ride Roller Coaster")
    age = int(input("What is your age: "))
    if age <12:
        bill = 5
        print("Child tickets: $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets: $7")
    elif (age >= 45) & (age <= 55):
        print("Elder tickets are free! :)")
    else:
        bill = 12
        print("Adult tickets: $12") 
        
    wants_photo = input("Do you want a photo clicked? Y or N: ")
    if wants_photo == 'Y':
        bill += 3
        
    print(f"Your total bill: ${bill}")
else:
    print("Do not Ride Roller Coaster!")
    
    
    



