tasks=[]


print("Welcome to richumons' TO DO list")

print("Options:-")
print("1. Add a task")
print("2. view upcoming tasks")
print("3. remove a task")

choice=int(input("Enter your choice: "))


if choice==1:
    task=input("Enter a task: ")
    tasks.append(task)

elif choice==2:
    print(tasks)

while True:

    print("Welcome to richumons' TO DO list")

    print("Options:-")
    print("1. Add a task")
    print("2. view upcoming tasks")
    print("3. remove a task")
    print("4. exit the program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)

    elif choice == 2:
        print(tasks)

    elif choice==3:
        print(tasks)
        taskos=input("Which task do you want to remove: ")
        tasks.remove(taskos)

    elif choice==4:
        break

    if choice>3:
     print("invalid choice")

