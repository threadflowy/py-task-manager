import sys

d = 1

def main():
    command = str(input('Please, type a command: ')).lower()

    cmds(command)

def cmds(command):
    match command:
        case '/help':
            help()

        case '/createtask':
            task = input('What do you want to do?\n')
            print()
            createTask(str(task))

        case '/showtasks':
            showTasks()

        case '/cleartasks':
            clearTasks()

            global d
            d = 1

        case '/exit':
            exit()

        case _:
            print(f'\nSomething went wrong! Probably your command isn`t exist.\nHere is all commands you can use:')
            help()

def help():
    print('\n/help: Views all available commands.\n'
            '/createtask: Creates one task.\n'
            '/showtasks: Shows your tasks.\n'
            '/cleartasks: Deletes all of your tasks.\n'
            '/exit: Exits the "Untitled task manager".\n')

def createTask(task):
    global d
    with open('tasks.txt', 'a', newline='') as tasks:
        tasks.write(f'{d}. {task}\n')
    
    print('Task created.\n')

    d += 1

def showTasks():
    with open ('tasks.txt', 'r') as tasks:
        print(f'\n{tasks.read()}')

def clearTasks():
    confirmClear = str(input('Are you sure you want to delete all of your tasks? y/n\n'))

    if confirmClear.lower() == 'y':
        try:
            with open ('tasks.txt', 'w') as tasks:
                tasks.write('')
            print('\nYou have deleted all your tasks.\n')

        except Exception as e:
            print(f"An error occurred: {e}")
    elif confirmClear.lower() == 'n':
        print('\nDeleting was canceled.\n')

def exit():
    confirmExit = str(input('Are you sure you want to exit "Untitled task manager"? y/n\n'))

    if confirmExit.lower() == 'y':
        print('\nExit confirmed...\n')
        sys.exit()
    elif confirmExit.lower() == 'n':
        print('\nExit canceled.\n')

if __name__ == '__main__':
    print('Hello! You are currently using the "Untitled task manager".')
    while (True):
        main()