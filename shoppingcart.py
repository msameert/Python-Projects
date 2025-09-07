"mini shopping cart system that contains varablrs, lists, loops, conitions and functions"

items = {
    "apple": 50,
    "banana": 70,
    "orange": 30,
    "carrot": 60,
    "meat": 40
}
cart =[]  #empty list

def addtocart():
 choice = input("Write the item name: ")
 if choice in items:
    print(f"You have selected :",[choice])
    cart.append(choice)
 elif choice not in items:
    print("Item Not in menu")

def remove_item():
 choice = input("Write the item name you want to remove : ")
 if choice in items:
    print(f"You have selected :",[choice])
    cart.remove(choice)

def bill():
  total = 0
  for item in cart :
      total += items[item]
  print(f"Your total bill is : {total}")
  
def menu():
  while True:
   print("\n\nWelcome To Shopping Cart\n")
   print("1. Show Menu")
   print("2. add an item to cart")
   print("3. Remove an item from cart")
   print("4. Show cart")
   print("5. Exit")

   choice = input("kindly select your option : ")

   if choice == "1":
    print(items)
   elif choice == "2":
    addtocart()
   elif choice == "3":
     remove_item()
   elif choice == "4":
     print(cart)
   elif choice == "5":
     print("Thank you for shopping")
     bill()
     break 
 

menu()