# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:14:07 2023
@author: Luvkush
"""

start_number = input("Enter the start number: ").strip()
end_number = input("Enter the end number: ").strip()
number_to_count = input("Enter digit to count: ").strip()

def digits_counter(start, end, digit_to_count):
    
    counter = 0
    
    for value in range(start, end+1):
        temp = value
        while(temp!=0):
            
            rem = temp%10
            quo = temp//10
            temp = quo
            
            if rem == digit_to_count:
                counter += 1
    return counter
            
        
try:
    start_number = int(start_number)
    end_number = int(end_number)
    number_to_count = int(number_to_count)
except Exception as e:
    print(f"\nError: {e}: Please enter integer only without characters or symbols!")
else:
    result = digits_counter(start_number, end_number, number_to_count)
    print(f"\nThe digit {number_to_count} appears {result} times between {start_number} and {end_number}.")
        
            
    