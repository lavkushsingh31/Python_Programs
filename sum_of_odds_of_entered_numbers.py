# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:03:11 2023
@author: Luvkush
"""

def collect_ints_from_user():
    entered_numbers = []
    print("Please keep entering numbers to calculate sum of odds, and 'q' to quit...\n")
    while(True):
        user_input = input().strip()
        
        if user_input.lower() == 'q':
            break
        else:
            try:
                user_input = int(user_input)
            except Exception as e:
                print(f"Error: {e}: Please enter integers without any character or symbol!")
            else:
                entered_numbers.append(user_input)
    return entered_numbers

def sum_of_odds(lst):
    sum_of_odds = 0
    for num in lst:
        if num%2 != 0:
            sum_of_odds += num
    return sum_of_odds
               
user_numbers = collect_ints_from_user()
result = sum_of_odds(user_numbers)

print(f"\nSum of Odd numbers: {result}")
        
    
    