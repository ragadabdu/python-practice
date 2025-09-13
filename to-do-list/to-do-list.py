# To-Do-List program

tasks = [] 

while True:  #<--loop
    action = input("Mark complete? Delete? Add? View? Reset date? Exit?: ") #<--menu 
    if action == "exit": 
        break

    elif action == "Mark complete":
        index = int(input("Enter index: "))    #<-- set a task as complete by asking for the index and calling the "state" dictiontary
        tasks[index]["state"]="complete"

    elif action == "delete":
        index = int(input("Enter index: ")) #<--using pop to remove specific item in a list
        tasks.pop(index)

    elif action == "add":
        tasks.append({"task": input("Enter task: "), "state": "incomplete", "due date": input("due date: ")}) #<--tasks is a list of dictionaries

    elif action =="view":
        for index, task in enumerate(tasks): 
            print(f"{index}. {task['task']} - {task['state']} - {task['due date']}") 

    elif action == "reset":
        index = int(input("Enter index: "))
        tasks[index]["due date"] = input("reset due date: ")

    else:
        print("Invalid action")




