from task_manager import TaskManager

Flag = {
    "status" : True
}

def addTaskFn(title):
    t = TaskManager()
    t.add_task(title)
    
def operation(op):
    if(op == 1):
        title = input("Enter the title")
        addTaskFn(title)

    elif(op == 2):
        Flag["status"] =False
    else:
        print("Reselect")
    
def main():
    option = int(input('Enter the selection 1)Add a task 2)Exit'))
    operation(option)


if __name__ == '__main__':
    print(Flag)
    while(Flag["status"]):
        main()