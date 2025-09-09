import random
accInfo = []

while True:
    action = input("choose acc action: Add? View? Delete? Exit? ")

    if action == "exit":
        break

    elif action == "add":
        accInfo.append({"Name": input("Enter acc name: "), "Password":input("Enter acc pass: ")})

    elif action == "view":
        for index, acc in enumerate(accInfo):
            print(f"{index}. {acc['Name']}, {acc['Password']}")
    else:
        print("invalid action")

