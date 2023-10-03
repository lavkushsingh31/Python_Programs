# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:46:51 2023
@author: Luvkush
"""

zodiac_sign = {
    0: "Monkey",
    1: "Rooster",
    2: "Dog",
    3: "Pig",
    4: "Rat",
    5: "Ox",
    6: "Tiger",
    7: "Rabbit",
    8: "Dragon",
    9: "Snake",
    10: "Horse",
    11: "Goat"    
    }

year = int(input("Enter Year: "))

zodiac = year%12 
print(f"Your Zodiac Sign : {zodiac_sign[zodiac]}")

