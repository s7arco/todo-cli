FILE_NAME = "tasks.txt"
options = {1: "View tasks", 2: "Add task", 3: "Remove task", 4: "Quit"}

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
     if not tasks:
        print("There are no tasks!")
     else: 
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        
def add_task(tasks):
    task = input("What task would you like to add? : ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"{task} has been added to Tasks!")
    
def remove_task(tasks):
    if not tasks:
        print("There are no tasks to remove!")
        return
    
    view_tasks(tasks)
    
    try:
        task_number = int(input("Which task would you like to remove? : "))
    except ValueError:
        print("Write a valid number!")
        return
    
    if not 1 <= task_number <= len(tasks):
        print("Tasks doesnt exist!")
        return
    else:
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}")
    
tasks = load_tasks()

while True:
    print("=== To-Do List ===")
    for number, name in options.items():
        print(f"{number}. {name}")
    try:
        choice = int(input("What would you like to do? : "))
    except ValueError:
        print("Write a valid input!")
        continue
    
    if choice not in options:
        print("Pick from one of the options!")
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print(f"You chose: {options[choice]}")
        
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            remove_task(tasks)  
