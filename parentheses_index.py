# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:09:43 2023
@author: Luvkush

Input:
()(())

Output:
[1, 0, 5, 4, 3, 2]
"""

string = input("Enter the string with Parenthesis: ")

def index_finder(strng, charr):
    return [i for i, ltr in enumerate(strng) if ltr == charr]

for index, char in enumerate(string):
    
    if char == "(":
        f_idx = index
        b_idxs = index_finder(string, ")")
        
        for b_idx in b_idxs:
            if b_idx-f_idx == 1:
                string = string.replace("(", str(b_idx),1)
                string = string.replace(")", str(f_idx),1)
                break
            else:
                val = (b_idx-f_idx)*2
                b_idx = f_idx+val-1
                string = string.replace("(", str(b_idx),1)               
                x = list(string)
                x[b_idx] = str(f_idx)
                string = "".join(x)
                break
result = list(map(lambda x: int(x), list(string)))
print(result)
            