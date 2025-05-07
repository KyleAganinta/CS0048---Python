

def addTask(task, list):
    list.append(task)

def viewTask(list):
    print(list)

def removeTask(task, list):
    list.remove(task)

task_list = []
while True:
    print("Welcome to To-do-list maker\n1. Add task\n2. Remove task\n3. View tasks\n4. Exit")

    choice = int(input("Input your choice: "))



    if choice == 1:
        task = input("\nInput task to do: ")
        addTask(task, task_list)
        print("Task added\n")
    
    elif choice == 2:
        task = input("Input task to remove: ")
        if len(task_list)==0: 
            print("\nNo tasks yet\n")

        elif task not in task_list:
            print("\nTask not present in list\n")
        
        else:
            removeTask(task, task_list)
            print("\nTask removed.\n")

    elif choice == 3:
        if len(task_list)==0: 
            print("\nNo tasks yet\n")
        
        else:
            viewTask(task_list)
            print("")
    
    elif choice == 4:
        print("\nThanks for using To-do-list")
        break
    
    else:
        print("Invalid input")


