

class Employee:
   def  __init__(self, name, role, department, salary):
      self.name = name
      self.role = role
      self.department = department
      self.salary = salary

   def showdetails(self):
      print(self.name)
      print(self.role)
      print(self.department)
      print(self.salary)

print("Employee 1")
employe1 = Employee("sameer","CEO","company","censored")
employe1.showdetails()

print("Employee 2")
employe2 = Employee("abdullah", "CEO", "company", "censored")
employe2.showdetails()