"made stopwatch and countdown program"
import time 


def countdown():
 timer = int(input("Enter seconds you wanna countdown :"))
 while True:
  
  if timer > 0 :
   timer -=1
   time.sleep(1)
   print(f"the time is {timer} :")
  elif timer == 0:
   print("Time's up-")
   break


def stopwatch():
   
   try:
    
     timer = 0
     while True:
       timer += 1
       time.sleep(1)
       print(f"The time is {timer}")
   except KeyboardInterrupt:
       print('Stopped')
    

def menu():
  while True:
   print("Welcome")
   print("1.Countdown")
   print("2.Stopwatch")
   print("3.Exit")

   choice = input("Select option: ")

   if choice == "1":
    countdown()
   elif choice == "2":
    print("press Ctrl + C to stop countdown")
    stopwatch()
   elif choice == "3":
    print("Thank you")
    break

menu()