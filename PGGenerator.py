# Import the random module
import random
# Import the string module
import string

length = int(input("Enter the length of your password: "))

print('''Choose what kinds of characters you'd like to include in your password:
1. Generate a password with uppercase letters, lowercase letters, numbers, and special characters.
''')

characterlist = ""

# Getting the character list for the password
while(True):
    choice = int(input("Press 1 to generate your password: "))
    if (choice == 1):
        characterlist += string.ascii_letters + string.digits + string.punctuation
        
    else:
        print("Invalid choice. Please try again.")
    
    password = []

    for i in range(length):
        # Picking a random character from the list
        random_character = random.choice(characterlist)
        password.append(random_character)

        # Appending a random character to the password
        password.append(random_character)

    # Printing the generated password
    print("Your randomly generated password is: " + "".join(password))
    break