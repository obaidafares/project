import utils

while True:
    try:
        choice = int(input("""
menu :

1. Add Task
2. View Tasks
3. Delete Task
4. Update Task
5. Save Tasks
6. Exit

    please enter a number [1-5] : """))
    except ValueError:
        print("Please enter a number .")
        continue
    
    if choice == 1:
        utils.add_task()
    elif choice == 2:
        
        utils.View_Tasks()
    elif choice == 3:
        utils.Delete_Task()
    elif choice == 4:
        utils.Update_Task()
    elif choice == 5:
        utils.Save_Tasks()
    elif choice == 6:
        utils.exit()
        break
    else:
        print("Please enter a number between 1 and 5 .")
    
    







