# -*- coding: utf-8 -*-
"""
Created on Mon May  1 02:28:30 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""


print(" ***** Welcome to the Love Calculator! *****\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

t_count = name1.count('t') + name2.count('t')
r_count = name1.count('r') + name2.count('r')
u_count = name1.count('u') + name2.count('u')
e_count = name1.count('e') + name2.count('e')

l_count = name1.count('l') + name2.count('l')
o_count = name1.count('o') + name2.count('o')
v_count = name1.count('v') + name2.count('v')


true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

love_score = 10*true_count + love_count

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

          
