import time
import uuid
from services import IOFile

def logcall(func):
    def wrapper(*args,**kwargs):
        results = func(args,kwargs)
        print('results',results)
        return("values arg:{} kwarg:{}".format(args,kwargs))
    return wrapper

def details(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print("Res",result)
        return result
    return wrapper


class Task:
    def __init__(self,title):
        self.id = str(uuid.uuid4())
        self.title = title
        self.createdAt = time.time()
        self.done = False
   

    def check(self):
        print(self)


taskLists = []
class TaskManager:



    @details
    def watch(self):
        print("------------",taskLists)
        for item in taskLists:
            print(item)


    def view_tasks(self):
        iof = IOFile()
        

    def add_task(self,title):
        t = Task(title)

        taskLists.append({
            "id" : t.id,
            "title" : t.title,
            "createdAt": t.createdAt,
            "done" : t.done,
        }
        )
        iof = IOFile()
        iof.add_content({
            "id" : t.id,
            "title" : t.title,
            "createdAt": t.createdAt,
            "done" : t.done,
        })
        print("Added a task")
    

    
        # return taskLists
        # return watch(t)
        



if __name__ == '__main__':
    print("task Manager")