import random,string
accInfo = []

def generate_password(length=8):
    characters = string.ascii_letters + string.digits 
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    action = input("choose acc action: Add? View? Delete? Exit? ")

    if action == "exit":
        break

    elif action == "add":
        name = input("Enter acc name: ")
        choice = input("Do you want to generate a password? (yes/no): ")
        if choice == "yes":
            password = generate_password(12)
            print("Generated password:", password)
        else:
            password = input("Enter acc pass: ")
            accInfo.append({"Name": name, "Password": password})

    elif action == "view":
        for index, acc in enumerate(accInfo):
            print(f"{index}. {acc['Name']}, {acc['Password']}")
    else:
        print("invalid action")

