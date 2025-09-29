"""Dice Simulator and calculating frequencies and probabilities of each number"""

import numpy as np

def dice_simulator():
 rolls = int(input("Enter how many times you wanna roll a dice : "))

 results = np.random.randint(1,7,size = rolls)

 values, counts = np.unique(results, return_counts=True)

 probabillities = counts / rolls

 print("Dice Simulation Results")
 for value, count, prob in zip(values, counts, probabillities):
  print(f"Number {value}-> Count: {count}, Probability: {prob:.2f}")
 
 print("\nTheoretical Probability of each number = 1/6 ≈ 0.167")


dice_simulator()