"""Password strength checker - criteria : should have 8 digits, uppercase, lowercase, number, special characters like @!&* """

strength = 0

password = input("Enter your password : ")

if len(password) >= 8:
    strength += 1
    
else :
    print("Password must be 8 digit")

if any(char.isupper() for char in password):
    strength += 1
else :
    print("Password must have upper letter")

if any(char.isdigit() for char in password):
    strength += 1
else : 
    print("Password must contain integer")

if any(not char.isalnum() for char in password):
    strength += 1
else :
    print("Password must contain special character")

if any(char.islower() for char in password):
    strength += 1
else :
    print("Password should have lowercase")


if strength == 5:
    print("Password strength is strong")
elif strength == 4:
    print("Password is Less stronger")
elif strength == 3:
    print("Password strength is Medium")
elif strength == 2:
    print("Password is Weak")
elif strength == 1:
    print("Password is very Weak")
else :
    print("Invalid Password")
