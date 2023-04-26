# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:48:54 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

print("Hello Spyder IDE!")
print("Day 1 - Python Print Function")
print('The function is declared like this:')
print("print('what to print')\n\n")


print('Testing.\nThis should be line\nThis is line 3\n\n')


print('Lets '+ 'concatenate!\n\n')

user_input = input("What is your name? : ")
print('Hello, '+user_input+'!\n\n')

print(len(input("What is your name? ")))

# Implementation of Swapping variable values

a = input('\n\nEnter the value of \'a\': ')
b = input('Enter the value of \'b\': ')

temp = a
a = b
b = temp

print(f'a: {a}')
print(f'b: {b}')


# Band name Generator

print('\n\nHello!\n')
city = input('Enter your birth city: ')
pet = input('Enter your pet name: ')

print(f'Your band name is: {city} {pet}')
