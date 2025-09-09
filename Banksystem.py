"""  Banking System That can access multiple users/accounts - used class, functions and loops  """

class BankAccount :

    
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account
    
    def balance2(self):
        return f"Your balance is {self.balance}"

    def credit(self):
        add = int(input("Enter amount : "))
        self.balance += add
        return f"Your new balance is : {self.balance}"



def menu(bankacc1):
 
 while True:
  print("Menu")
  print("!. Check Balance")
  print("2. Add amount ")
  print("3. Exit")
  choice =  input("Select option : ")
  if choice =="1":
     
    print(bankacc1.balance2())
  if choice == "2":
  
    print(bankacc1.credit())
  if choice == "3":
     break

account = BankAccount(20000, 2233)
account2 = BankAccount(30000, 2234)

 
def menu_real():
  while True:
    print("\n🏦 Welcome to the Bank System")
    print("1. Access Account 2233")
    print("2. Access Account 2234")
    print("3. Exit")

    main_choice = input("Choose account: ")

    if main_choice == "1":
        menu(account)
    elif main_choice == "2":
        menu(account2)
    elif main_choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")




menu_real()

