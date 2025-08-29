""" ATM Machine that can check balance, deposit, pin verification, and exit thee loop """

balance = 10000

def check_balance():
    global balance
    print("\nyour balance is :", balance)

def add_amount():
    global balance
    deposit = float(input("How much do you want to deposit :"))
    balance += deposit
    print("\nYour new balance is :", balance)

def withdraw_amount():
    global balance
    withdraw = float(input("How much do you want to withdraw :"))
    balance -= withdraw
    print("\nYour new balance is :", balance)
    
def menu():
    while True:
     print("1. Check Balance: \n2. Deposit balance : \n3. Withdraw balance : \n4. Exit")
     a =  input("\nSelect option :")
     if a == "1":
        check_balance()
     elif a == "2":
        add_amount()
     elif a == "3":
        withdraw_amount()
     elif a == "4":
        print("\nThank you for using ATM machine")
        exit()
        break
        
def pin_verify():
    while True:
        pin = input("Enter pin:")
        if pin == "1234" :
            menu()
            break
        else:
            for attempts in range(3):
                if attempts < 2:
                    pin = input("Incorrect pin \nEnter Pin again:")
                else:
                    print("Too many incorrect attempts. Account Locked.")
                    exit()
            print("Incorrect pin, please try again.")
       
       
pin_verify()