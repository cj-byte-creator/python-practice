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
    with open("Task_Manager/tasks.json","w") as f:
        json.dump(tasks,f,indent=4)
    choice = input("Input the number of your choosing : ")
    match choice:
        case "1":#Adding tasks
            task_name = input("Input task title/name : ")
            task = Task(task_name)
            tasks.append(task.to_dict())
            print("Task added!")
            continue
        case "2":#Printing all tasks
            if tasks == []:
                print("No Tasks yet")
                continue
            else:
                print("---Tasks---")
                i = 1
                for task in tasks:
                    print(f"{i}. {task["title"]} {"[ / ]" if {task["is_completed"]} == True else "[  ]"}")
                    i += 1
                continue
        case "3":#Marking tasks as done
            print("Not Implemented Yet!")
            continue
        case "4":#Exiting the program
            break
        case _:#Invalid Input Checker
            print("-----Write a valid number.-----")
            continue

print("-----Thank you!-----")


# print(user_list)




