# Password Strength Checker
# This program checks password strength .
#  guides the user to improve it
# This program checks password strength and guides the user to improve it


password = input("Enter your password: ")

# Rule 1: No spaces allowed
if " " in password:
    print("Invalid password: Spaces are not allowed.")
    print("Please enter a password without spaces.")
    exit()

# Rule 2: Password length must be exactly 8
if len(password) != 8:
    print("Invalid password length.")
    print("Password must be exactly 8 characters long.")
    exit()

# Flags to track character types
has_letter = False
has_number = False
has_special_char = False

# Check each character in the password
for char in password:
    if char.isalpha():
        has_letter = True
    elif char.isdigit():
        has_number = True
    else:
        has_special_char = True

# Final validation with user-friendly messages
if has_letter and has_number and has_special_char:
    print("Strong password ")
else:
    print("Weak password ")
    print("To make your password strong, include:")
    
    if not has_letter:
        print("- At least one letter (a-z or A-Z)")
    if not has_number:
        print("- At least one number (0-9)")
    if not has_special_char:
        print("- At least one special character (!, @, #, etc.)")
