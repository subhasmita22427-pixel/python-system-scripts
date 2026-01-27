# Password Strength Checker
# This program checks how strong a password is
# It checks length, numbers, and special characters

password = input("Enter your password: ")

# Check the length of the password
password_length = len(password)

# Flags to check conditions
has_number = False
has_special_char = False

# Go through each character in the password
for char in password:
    if char.isdigit():
        has_number = True
    elif not char.isalnum():
        has_special_char = True

# Decide password strength
if password_length >= 8 and has_number and has_special_char:
    print("Strong password")
elif password_length >= 6:
    print("Moderate password")
else:
    print("Weak password")
