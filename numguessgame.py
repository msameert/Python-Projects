""" Number Guessing Game using random library """


import random


def number_game():
 number = random.randint(1,100)
 print("Welcome to Number guessing game!")

 while True:
  guess = int(input("Guess the number :"))

 
  if guess > number :
        print("The guess is bigger than number")
  elif guess < number :
        print("The guess is smaller than number")
  else :
        print("Your guess is right")
        break