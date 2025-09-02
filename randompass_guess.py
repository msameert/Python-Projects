""" random password suggester using random and string lilbraries """

import random 
import string

print("This program gives Strong and Valid Password having character, special digits, numbers, uppercase, and lowercase")
while True:
 password_intake = input("Press Y if you want random  password : ")

 if "Y" in password_intake:
    chars = string.ascii_letters + string.digits + string.punctuation
    random_generator = str(random.choices(chars, k=9))
    #password = "".join(random_generator)
    print(random_generator)
    
 else :
   break




