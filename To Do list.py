#if statement with their input if they finish their task keep it else remove by [import os, .remove (Thing)] 
import os
file = 'tasks.txt'
with open("tasks.txt", "w") as file:
    def add_task():
        task = int(input("Enter the number of tasks to be added:"))
        if task > 0:
            with open("tasks.txt", "a") as file:
                for i in range(task):
                    task_name = input(f"Enter task {i + 1}: ")
                    file.write(task_name + "\n")
                    print(f"Task added Successfully.\n")
        else:
            print("\"Illegal\" number of tasks!") 
    def view_tasks():
        sel = input("If you want to view a specific task typr[1] or if you want to view full list type[2]:")
        if sel == '1':
            if os.path.exists("tasks.txt"):
                with open("tasks.txt", "r") as file:
                    task = file.readlines()
                    m = int(input("Enter the task number you want to view: "))
                    n = m-1
                    if n >= 0 and n < len(task):
                        print(f"The task at",m,"is:","\"",task[n].strip(),"\"")
                    else:
                        print("There's no such task in that number exists.")
            else:
                print("No tasks found.")
        elif sel == '2':
            with open("tasks.txt", "r") as file:
                if os.path.exists("tasks.txt"):
                    task = file.read()
                    print("Your tasks are:\n", task.strip())
                else:
                    None
    def remove_task():
        if os.path.exists("tasks.txt"):
            with open ("tasks.txt", "r") as file:
                p = input("Enter [1] to remove a specific task or [2] to remove all the tasks:")
                if p == '1':
                    with open("tasks.txt", "r") as file:
                        task = file.readlines()
                        with open("tasks.txt", "w") as file:
                            q = int(input("Enter the task number you want to remove:"))
                            r = q-1
                            if r >= 0 and r < len(task):
                                rem = task.pop(r)
                                print(f"Removed Successfully")
                            else:
                                print("There's no such task in that number exists.")
                elif p == '2':
                    with open("tasks.txt", "w") as file:
                        file.truncate(0)
                        print("All tasks removed successfully.")
        else:
            None
    def update_task():
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                task = file.readlines()
                if len(task) == 0:
                    print("No tasks to update.")
                    return
                with open("tasks.txt", "w") as file:
                    q = int(input("Enter the task number you want to update:"))
                    r = q-1
                    if r >= 0 and r < len(task):
                        s = input("Enter the updated task: ")
                        task[r] = s + "\n"
                        file.writelines(task)
                        print(f"Task {q} updated successfully.")
                    else:
                        print("There's no such task in that number exists.")
        else:
            print("No tasks found to update.")
    def exit():
        while True:
            print("Seeya buddy, have a nice day!")
            exit()
            break
            

    def main():
        while True:
            print("To do list menu select one from the following options to add task[1] . to view task[2] . to remove task[3] . to update task[4] . to exit[5]")
            choice = input("Enter your choice: ")
            add_task() if choice == '1' else view_tasks() if choice == '2' else remove_task() if choice == '3' else update_task() if choice == '4' else exit() if choice == '5' else print("Invalid choice, please try again.")
    main()