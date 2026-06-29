tasks=[]
while True:
    print("\n--TO-DO List--")
    print("1.Add Taask")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")
    choice=input("enter your choice")
    if choice=="1":
        task=input("Enter a task:")
        tasks.append(task)
        print("Task added successfully!")
    elif choice=="2":
        if len(tasks)==0:
            print("No tasks available")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])
            num=int(input("enter task number to remove:"))
            if num>0 and num<=len(tasks):
                removed=tasks.pop(num-1)
                print(removed,"removed successfully")
            else:
                print("Invalid task number")
    elif choice=="4":
        print("Thank you!")
        break
    else:
        print("Invalid choice")