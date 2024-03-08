def get_todos(filepath):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
        return local_todos

def write_todos(filepath, todos_args):
    with open("todos.txt", 'w') as file:
        file.writelines(todos_args)

if __name__ =="__main__":
    print(type("Hello"))