import time
from functions import get_todos,write_todos
now = time.strftime("%d %M %Y %H:%M:%S")
current_hour =int(time.strftime("%H"))

if 5 <= current_hour < 12:
    greeting ="Good Morning"

elif 12 >= current_hour <= 4:
    greeting ="Good Afternoon"

else :
    greeting ="Good Night"

print(f"{greeting} The Current time is :{now}")

while True:
    user_action = input("Type add or show or edit or Complete or exit :")
    user_action: str = user_action.strip()
    if user_action.startswith('add'):
        # if 'add' in user_action:
        # this in operator is used for the checking if the given word in indentation contains in the string or not
        todo = user_action[4:]
        # with open("todos.txt",'r') as file :    #so if the program stops at some point so with this context manager the file will be closed so it the benefit of this
        # todos = file.readlines()   # it reads the lines
        todos = get_todos("todos.txt")
        todos.append(todo)  # appends the list to the todo # we are making a change in the file here
        write_todos("todos.txt",todos)
        #with open("todos.txt", 'w') as file:  # and here we are opening the file
         #   todos = file.writelines(todos)  # here the whatever the changes made in file are overwritten

    elif user_action.startswith('show'):
        #   ('show' in user_action):
        # with open("todos.txt", 'r') as file:
        # todos = file.readlines()
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            new_item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            # 'edit' in user_action):
            number = int(user_action[4:])
            print(number)
            number = number - 1

            # with open("todos.txt", 'r') as file:
            # todos = file.readlines()
            todos = get_todos("todos.txt")
            print('here is todo existing', todos)

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo + '\n'
            write_todos("todos.txt",todos)

            print('the new todo after editing will be', todos)
           # with open("todos.txt", 'w') as file:
            #    todos = file.writelines(todos)
        except ValueError:
            print("Your Command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            # 'complete' in user_action):
            number = int(user_action[9:])
            # here we have used list slicing so that we can print after the what comes after the
            # complete command
            # like for ex the command complete has indexcing of 8 with the space it is 9.

            # with open("todos.txt", 'r') as file:
            # todos = file.readlines()
            todos = get_todos("todos.txt")
            index = number - 1
            todos_to_remove = todos[index]
            todos.pop(index)
            write_todos("todos.txt",todos)

            #with open("todos.txt", 'w') as file:
             #   todos = file.writelines(todos)
            message = f"Todo {todos_to_remove} has been removed"
            print(message)
        except IndexError:
            print("There is no Such Item in the todo list")
            continue
    elif user_action.startswith('length'):
        print(len(todos))
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
