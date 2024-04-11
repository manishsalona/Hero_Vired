import re

def check_password_strength(password):
    
    if len(password) < 8:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[!@#$%]", password):
        return False
    
    return True

# Script to take user input and validate password strength
password = input("Enter your password to check its strength: ")

if check_password_strength(password):
    print("Your password is strong.")
else:
    print("Your password is weak. Make sure it is at least 8 characters long, contains both uppercase and lowercase letters, has at least one digit, and includes at least one special character (!, @, #, $, %).")

