"""
Unit converter that converts ;
 Miles <-> KiloMeters,
 Celsius <-> Fahreheit,
 Kilograms <-> Pounds, 
 Meters <-> Feet, 
 Liters <-> Gallons 
"""


def miles_to_KM() :
   miles = float(input("Enter Miles you want to convert into Kilometres : "))
   kilometres = miles*1.609
   print(f" Converted {miles} miles into kilometers are : {kilometres} kilometers")


def KM_to_miles():
   kilometres = float(input("Enter Kilometers you want to convert into miles : "))
   miles = kilometres*0.621371
   print(f"Converted {kilometres} kilometeres into miles are : {miles} miles")

def Celsius_to_Fahrenheit():
   celsius = float(input("Enter Celsius Temperature to convert into Fehrenheit : "))
   fahrenheit = (celsius*9/5) + 32
   print(f"Converted {celsius} Celsius Temp into Fahrenheit Temp which is : {fahrenheit} Fahrenhiet Temp")

def FR_to_Celsius():
   fahrenheit = float(input("Enter Fahrenheit to convert into Celsius : "))
   celsius = (fahrenheit - 32)* 5/9
   print(f"Converted {fahrenheit} Fahrenheit Temp into Celsius Temp which is : {celsius} celsius Temp")

def KG_to_pounds():
   kilograms = float(input("Enter Kilograms you want to convert into pounds : "))
   pound = kilograms*2.205
   print(f"Converted {kilograms} kilograms into pounds are : {pound} pounds")

def pounds_to_kg():
   pounds = float(input("Enter pounds you want to convert into kilograms : "))
   kilograms = pounds/2.205
   print(f"Converted {pounds} pounds into kilograms are : {kilograms} kilograms")

def meters_to_feet():
   meters = float(input("Enter meters you want to convert into feet : "))
   feet = meters*3.281
   print(f"Converted {meters} meters into feet are : {feet} feet")

def feet_to_meters():
   feet = float(input("Enter feet you want to convert into meters : "))
   meters = feet/3.281
   print(f"Converted {feet} feet into meter are : {meters} meters")

def liters_to_gallons():
   liters = float(input("Enter liters you want to convert into gallons : "))
   gallons = liters/3.785
   print(f"Converted {liters} liters into gallons are : {gallons} gallons")

def gallons_to_liters():
   gallons = float(input("Enter liters you want to convert into gallons : "))
   liters = gallons*3.785
   print(f"Converted {gallons} gallons into liters are : {liters} liters")

def menu():
   while True:
      print("--Unit Converter app--")
      print("--Menu--")
      print("1. Convert Miles into Kilometers")
      print("2. Convert Kilometers into Miles")
      print("3. Convert Celsius into Fehrenheit")
      print("4. Convert Fehrenheit into Celsius")
      print("5. Convert Kilograms into Pounds")
      print("6. Convert Pounds into Kilograms")
      print("7. Convert Meters into Feets")
      print("8. Convert Feets into Meters")
      print("9. Convert Liters into Gallons")
      print("10. Convert Gallons into Liters")
      print("11. Exit")

      choose = int(input("Select the option : "))
      if choose == 1:
         miles_to_KM()
      elif choose == 2:
         KM_to_miles()
      elif choose == 3:
         Celsius_to_Fahrenheit()
      elif choose == 4:
         FR_to_Celsius()
      elif choose == 5:
         KG_to_pounds()
      elif choose == 6:
         pounds_to_kg()
      elif choose == 7:
         meters_to_feet()
      elif choose == 8:
         feet_to_meters()
      elif choose == 9:
         liters_to_gallons()
      elif choose == 10:
         gallons_to_liters()
      elif choose == 11:
         print("GoodBye ;)")
         break
         
      
menu()
        
         
