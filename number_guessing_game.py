# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:19:27 2023
@author: Luvkush
"""

import random

number_to_guess = random.randint(1, 100)
tries = input("Enter the number of tries you would like to have: ").strip()

try:
    tries = int(tries)
except Exception as e:
    print(f"Error: {e}: Please enter integer only without characters or symbols!")
else:
    print("\n")
    for attempt in range(1,tries+1):
        guessed_num = input(f"Attempt-{attempt}: Guess the number: ")
        
        if guessed_num.isdigit():
            guessed_num = int(guessed_num)
            if guessed_num == number_to_guess:
                print(f"\nYou guessed the secret number {number_to_guess} right in {attempt} attempts. Congratulations!! ")
                break
            elif guessed_num > number_to_guess:
                print("Too High! Try again.")
            else:
                print("Too Low! Try again.")
        else:
            print(f"You were supposed to enter integers! Your attempt {attempt} is lost, be careful in next attempt!")
        
        if attempt == tries:
            print("\nYou have exhausted your attempts. Thanks for playing!")
            break

