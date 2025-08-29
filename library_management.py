"library management system - enter pin, book list, add, remove and exit"

books = [
         "The Prince",
         "Rumi",
         "Power",
         "illusion of throne",
         "Mystical",
         "philosophy",
         "Alice in Wonderland",
         "Fictional sequnce"
          ]
borrowed_book = []


def show_books():

 print("The Books are :\n")
 for book in books:
    print("-", book)



def return_book():
    book = input("Enter the book you wanna add :")
    if book in borrowed_book: 
     books.append(book)
     borrowed_book.remove(book)

def borrow_book():
    book = input("Enter the book you wanna borrow :")
    if book in books:
        borrowed_book.append(book)
        books.remove(book)
        print(f"You borrowed this book called '{book}'")



def menu():

 while True: 
   
      
   print("Welcome to Library Management System")
   print("Menu")
   print("1. Show Books")
   print("2. Borrow Book")
   print("3. Return Book")
   print("4. Exit")


   choice = input("Select an option :")

   if choice == "1":
      show_books()
   elif choice == "2":
      borrow_book()
   elif choice == "3":
      return_book()
   elif choice == "4":
       print("Thank you")
       break
   else :
       print("Invalid option")
    

def verify():
 while True:
  
  pin = input("Enter Pin :")
  if pin == "1234":
    menu()
    break
  
  else :
    print("Invalid Pin. Try again :")
    

verify()