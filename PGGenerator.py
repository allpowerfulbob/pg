# Import required modules
import random
import string
length = int(input("Enter the length of your password: "))
print('''Generate a password with uppercase letters, lowercase letters, numbers,
      and special characters.''')
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
    print("Your randomly generated password is: " + "".join(password))
    break