# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:19:27 2025
@author: Luvkush
Title:  Write a program that takes a list of rolls as input for each player and 
calculate the average roll for each player.
"""

player_rolls = [
    [4, 2, 6, 3, 1],  # player 1's rolls
    [3, 5, 6, 4, 2],  # player 2's rolls
    [1, 2, 2, 6, 4]   # player 3's rolls
]

avg_rolls = {}

for player, rolls in enumerate(player_rolls, start=1):
    avg_rolls[f"Player_{player}"] = sum(rolls)/len(rolls)

print(avg_rolls)

print(max(avg_rolls, key=avg_rolls.get))

print(sorted(avg_rolls.items(), key=lambda x: x[1]))