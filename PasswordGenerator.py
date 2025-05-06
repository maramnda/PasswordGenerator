# This project:
# Generate a random password
# The password consist of digits, letters, and symbols
# User choose the length of the generated password

import random, string

def generatePassword(length = 12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    allChars = letters + digits + symbols
    # Endusre at least one characyer from each category
    password = [random.choice(letters),
                random.choice(digits),
                random.choice(symbols)
                ]
    password += random.choices(allChars, k = length - 3)
    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)

length = int(input("Enter a length for the password: "))
print("Your new password is: ", generatePassword(length))