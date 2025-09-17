" Student management system that contain menu system - it can add, view, search, and save data also error handling - "
" Structurally the code contains class, functions, loops, conditions, and file handling "

class Student:
    def __init__(self):
        self.name = input("Enter Student Name : ")
        self.rollno = input("Enter Roll No. of student : ")
        self.department = input("Enter Department of student : ")
        self.course = input("Enter the course of student : ")
        self.result = input("Enter The CGPA of student : ")
    
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.rollno}, Dept: {self.department}, Course: {self.course}, CGPA: {self.result}"


student_list = []
def add():
    n = int(input("How many students you wanna add : "))
    with open("student_data.txt", "a") as f:
     f.write("--Student Record-- \n")
     for i in range(n):
        print(f"Enter the details of the student - {i + 1}")
        student = Student()
        student_list.append(student)
        f.write(f"{i + 1}. Student Name: {student.name}, Roll No: {student.rollno}, Dept: {student.department}, Course: {student.course}, CGPA: {student.result}\n")
        
    print("\n -- All Students saved in Data Base/file --")

def view():
   if not student_list:
      print("--No students Found--")
   else:
    for student in student_list:
     print(student)

def search():
   n = input("Enter the Roll no of Student : ")
   found = False
   for student in student_list:
      if student.rollno == n:
         print(student)
         found = True
      if not found:
         pass
      
def remove():
   n = input("Enter Roll no of student you want to remove : ")


   for student in student_list:
      if student.rollno == n:
         student_list.remove(student)
         print("\n--Student Removed--")

      else:
         print("Student not found")

def load_data():
  try: 
     with open("student_data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
           if line.startswith("--") or line.strip() == "":
              continue
           parts = line.split(", ")
           if len(parts) == 5:
              name = parts[0].split(": ")[1]
              rollno = parts[1].split(": ")[1]
              department = parts[2].split(": ")[1]
              course = parts[3].split(": ")[1]
              result = parts[4].split(": ")[1]

              student = Student.__new__(Student)
              student.name = name
              student.rollno = rollno
              student.department = department
              student.course = course
              student.result = result
              student_list.append(student)
  except FileNotFoundError:
     pass

      
def menu():
   while True:
    print("--Welcome to Student Management System--\n")
    print("Kindly select the option below")
    print("1. Add a Student in the DataBase")
    print("2. View the record of all students")
    print("3. Search a paticular Student")
    print("4. Remove a student from Database")
    print("5. Exit")

    choice = input("Enter Option : ")
    if choice == "1":
      add()
    elif choice == "2":
      view()
    elif choice == "3":
      search()
    elif choice == "4":
      remove()
    elif choice == "5":
       break
    else :
      return "Invalid Option"  

load_data()
menu() 



       