# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:34:11 2023
@author: Luvkush
"""

start_number = input("Enter the start number: ").strip()
end_number = input("Enter the end number: ").strip()
number_to_count = input("Enter digit to count: ").strip()

def digits_counter_v2(start, end, digit_to_count):
    
    counter = 0
    digit_to_count = str(digit_to_count)
    
    for value in range(start, end+1):
        counter += str(value).count(digit_to_count)
        
    return counter
            
        
try:
    start_number = int(start_number)
    end_number = int(end_number)
    number_to_count = int(number_to_count)
except Exception as e:
    print(f"\nError: {e}: Please enter integer only without characters or symbols!")
else:
    result = digits_counter_v2(start_number, end_number, number_to_count)
    print(f"\nThe digit {number_to_count} appears {result} times between {start_number} and {end_number}.")
        
            
    