# Import the random module
import random
# Import the string module
import string

length = int(input("Enter the length of your password: "))

print('''Choose what kinds of characters you'd like to include in your password:
1. Uppercase letters
2. Lowercase letters
3. Numbers
4. Symbols
5. All of the above
''')

characterlist = ""

# Getting the character list for the password
while(True):
    choice = int(input("Enter your choice (1-5): "))
    if (choice == 1):
        characterlist += string.ascii_uppercase
    elif (choice == 2):
        chacterlist += string.ascii_lowercase
    elif (choice == 3):
        characterlist += string.digits
    elif (choice == 4):
        characterlist += string.punctuation
    elif (choice == 5):
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