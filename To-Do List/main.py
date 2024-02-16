tasks = []
choice = None


#creating a function that will add a task to the tasks list
def add_task(name, description, date_required=None, priority=0):
    task = {'Name':name, 'Description':description, 'Date Required':date_required,'Priority Level':priority }
    tasks.append(task)

#creating a function that will mark a task as complete and remove it from the list
def remove_task(name):
    global tasks
    tasks = [task for task in tasks if task['Name'] != name]


#creating a function that checks the tasks list for any task, if there are task in the list it will print the
#name,description, date it was submitted, date required, and its priority level. 
def display_task():
    if not tasks:
        print("No task on the list.")
    else:
        for i,task in enumerate(tasks, start=1):
            print(f"{i}. {task['Name']} - {task['Description']} - {task['Date Required']} - {task['Priority Level']}")
            print("Priority levels are set by '1 = HIGH','2 = MEDIUM','3 = LOW'\n")



def main():
    while True:
        print("Welcome to your personal to-do list! What would you like to do?")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n")
            name = input("Please enter the name of the task: ")
            description = input("Please enter the description of your task: ")
            date_required = input("Please enter the date this task needs to be completed by: ")
            priority_level = input("Please enter what priority level this task is: ")
            print("Priority level can be defined by '1 = HIGH','2 = MEDIUM','3 = LOW'")
            add_task(name,description,date_required,priority_level)

        elif choice == '2':
            print("\nCurrent list of tasks: ")
            display_task()
            name = input("What task would you like to remove: ")
            remove_task(name)
            print("\n")

        elif choice == '3':
            display_task()
            print("\n")
        
        elif choice == '4':
            print("\n")
            break
    
        else:
            print("Invalid choice. Please try again")

main()
            