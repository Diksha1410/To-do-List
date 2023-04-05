# Make a Python Project for "To-do List"
# Project Description :
# a. The code can add item to your to-do list
# b. The code can remove item from your to-do list
# c. It displays all our to-do tasks
# d. It can quit the program

# Code Starts Here:

# creating a empty list
todo_list = []
while True:
    # printing options to the users
    print("1: Add an item to list")
    print("2: Remove an item from list")
    print("3: SHow all the tasks")
    print("4: Quit")
    # prompt the user
    choice = input("Choose the option: ")

    if choice == "1":
        item = input("Add item to list: ")
        todo_list.append(item)
    elif choice == "2":
        index_str = input("Which item you want to remove(use index): ")
        index = int(index_str)
        todo_list.pop(index)
    elif choice == "3":
        for index, item in enumerate(todo_list):
            print(index,item)
    elif choice == "4":
        print("Quitting program.....")
    else:
        print("Please choose the appropriate option")