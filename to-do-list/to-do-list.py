tasks = []

while True:
    action = input("Mark complete? Delete? Add new task? View tasks? Exit?: ")
    if action == "exit":
        break

    elif action == "Mark complete":
        index = int(input("Enter index: "))
        tasks[index]["state"]="complete"

    elif action == "Delete":
        index = int(input("Enter index: "))
        tasks.pop(index)

    elif action == "Add new task":
        tasks.append({"task": input("Enter task: "), "state": "incomplete"})

    elif action =="View tasks":
        for index, task in enumerate(tasks):
            print(f"{index}. {task['task']} - {task['state']}")

    else:
        print("Invalid action")




