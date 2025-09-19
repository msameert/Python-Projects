import random 

def play():
    choices = ["rock","paper","scissor"]

    user_input = input("choose rock,paper,scissor : ")
    computer = random.choice(choices)
    print(f"Computer choosed :{computer}")

    if user_input == computer:
        print("Its a tie")
    elif (user_input == "rock" and computer == "scissor") or \
         (user_input == "paper" and computer == "rock") or \
         (user_input == "scissor" and computer == "paper"):
        print("You Win")
    else:
        print("you lose")
         
play()


