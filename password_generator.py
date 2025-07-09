import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        return "Error: No character types selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --------- Main Program ----------
print("🔐 Welcome to the Random Password Generator!")

try:
    length = int(input("Enter desired password length (e.g., 8–16): "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
        use_digits = input("Include NUMBERS? (y/n): ").lower() == 'y'
        use_special = input("Include SPECIAL characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_special)
        print("\n✅ Your Generated Password is:\n", password)

except ValueError:
    print("❌ Please enter a valid number for length.")
