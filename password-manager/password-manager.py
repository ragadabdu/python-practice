# Password-manager program
import random, string #<--import modules , string = 

accInfo = [] #<--a list for accounts

def generate_password(length=8):  #<--function to generate random passwords in 8 charachters, diff set of  upper case, lower case and digits
  
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    action = input("choose acc action: Add? View? Delete? Exit? ").lower() #<--menu

    if action == "exit":
        break

    elif action == "add":
        name = input("Enter acc name: ")
        choice = input("Do you want to generate a password? (yes/no): ").lower() 
        if choice == "yes":
            password = generate_password() 
            accInfo.append({"Name": name, "Password": password}) #<--append generated pass to the list of dictionaries
            print("Generated password:", password)
        else:
            while True:
                password = input("Enter acc pass: ")
                #password strength validator
                if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password):
                    accInfo.append({"Name": name, "Password": password}) 
                    break
                else:
                    print("Weak password. Try again.")

    elif action == "view":
        for index, acc in enumerate(accInfo):
            print(f"{index}. {acc['Name']}, {acc['Password']}")
    else:
        print("invalid action")

