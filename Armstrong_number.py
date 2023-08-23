# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:11:48 2023
@author: Luvkush
"""

num = int(input("Enter the number: "))

entered_num = num
cubesum = 0 

if num>=0:
    while (num/10 !=0):
        rem = num%10
        quo = num//10
        
        #print(f"Current Digit: {rem}")
        #print(f"Bacha hua number: {quo}")
        cubesum = cubesum+(rem**3)
        num = quo
        #print(f"This number goes for condition check: {num}")
        #print("\n")
        
        

if entered_num == cubesum:
    print("Number is Armstrong")  #0, 1, 153, 370, 371 and 407
else:
    print("Number is not Armstrong")