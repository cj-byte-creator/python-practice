import json
import os

if os.path.exists("Task_Manager/tasks.json") and os.path.getsize("Task_Manager/tasks.json") > 0:
    with open("Task_Manager/tasks.json", "r") as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            tasks = []
else:
    tasks = []

class Task:
    def __init__(self,title,is_completed=False):
        self.title = title
        self.is_completed = is_completed

    def to_dict(self):
        return self.__dict__
    
print("-----Welcome to the Task Manager!-----")
print("You can : \n 1. Add Task \n 2. View all Tasks \n 3. Mark tasks as done \n 4. Exit \n")

while True:
    choice = input("Input the number of your choosing : ")
    match choice:
        case "1":#Adding tasks
            task_name = input("Input task title/name : ")
            new_task = Task(task_name)
            tasks.append(new_task.to_dict())
            with open("Task_Manager/tasks.json","w") as f:
                json.dump(tasks,f,indent=4)
            print("Task added!")
        case "2":#Printing all tasks
            if tasks == []:
                print("No Tasks yet")
            else:
                print("---Tasks---")
                for i, task in enumerate(tasks,1):
                    status = "[ / ]" if task["is_completed"] else "[  ]"
                    print(f"{i}. {task["title"]} {status}")
        case "3":#Marking tasks as done
            print("Not Implemented Yet!")
        case "4":#Exiting the program
            with open("Task_Manager/tasks.json","w") as f:
                json.dump(tasks,f,indent=4)
            break
        case _:#Invalid Input Checker
            print("-----Write a valid number.-----")

print("-----Thank you!-----")



