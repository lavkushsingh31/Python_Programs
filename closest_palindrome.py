# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:49:52 2025
@author: Luvkush
Title: Program to find closest Palindrome of entered string
"""

string = input("Enter string: ")

if len(string)%2 != 0:
    mid = int((len(string)/2)-0.5)
    #print(mid)
    palindrome = string[:mid+1] + string[mid-1::-1]
    
print(f"Closest Palindrome: {palindrome}")