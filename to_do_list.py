""" to do list - task manager - add, done, or remove tasks"""



list = []
def add():
    task_input = input("Enter your new task : ")
    list.append(task_input)

def view_list():
    if not list:
     print("No task found")
    else :
       for i, task in enumerate(list, 1):
          print(f"{i}. {task}")

def done():
   n = int(input("Enter the Task you completed : "))
   if 1 <= n <= len(list):
      removed = list.pop(n - 1)
      print(f"Removed task : {removed}")
   else :
      print("Invalid task number")


def menu():
   while True:
      print("--WElcome to to do list--")
      print("Menu")
      print("1. Add task")
      print("2. View Task")
      print("3. Remove Completed Task")
      print("4. Exit")
      
      sel = int(input("Select option : "))
      if sel == 1:
         add()
      elif sel == 2:
         view_list()
      elif sel == 3:
         done()
      elif sel == 4:
         break      
      
menu()
