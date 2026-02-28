import time
import uuid
from services import IOFile




class Task:
    def __init__(self,title):
        self.id = str(uuid.uuid4())
        self.title = title
        self.createdAt = time.time()
        self.done = False
   

    def check(self):
        print(self)


class TaskManager:
  
    def view_tasks(self):
        iof = IOFile()
        

    def add_task(self,title):
        print("TITLE in add_task in TaskManager class",title)
        t = Task(title)
        iof = IOFile()
        iof.add_content({
            "id" : t.id,
            "title" : t.title,
            "createdAt": t.createdAt,
            "done" : t.done,
        })
        print("Added a task")



if __name__ == '__main__':
    print("task Manager")