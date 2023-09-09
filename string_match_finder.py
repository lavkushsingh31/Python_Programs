# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:04:37 2023
@author: Luvkush
"""

string = 'aasdfasdghfasdasaasd'
to_find = 'asd'
length = len(to_find)
result = []

for i in range(0, len(string)):
    
    if to_find == string[i:length]:
        result.append(i)
    
    length+=1
    
print(result)
    

