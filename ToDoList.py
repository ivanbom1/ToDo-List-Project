from datetime import date

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
        self.date = date.today()

    def completed_print(self):
        return self.completed

    def date_print(self):
        return self.date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        for task in self.tasks:
            if task.completed:
                c_status = "✅"
            else:
                c_status = "❌"
            print(f"Title: {task.title}, Description: {task.description}, Completed: {c_status}, Date: {task.date}")

    def add_task(self, title, description, completed=False):
        new_task = Task(title, description, completed)
        self.tasks.append(new_task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)

    def sort_tasks(self):
        self.tasks.sort(key=lambda task: task.date, reverse=False)

    def tick_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True


todo_list = ToDoList()

start = True
while start == True:

    print("\n(1) - Show your tasks"
          "\n(2) - Add a task"
          "\n(3) - Remove a task"
          "\n(4) - Sort your tasks by date"
          "\n(5) - Tick a task"
          "\n(6) - Quit")
    op = int(input("Choose an operation: "))

    if op == 1:
        print("This is your tasks: ")
        todo_list.show_tasks()
    elif op == 2:
        title = input("Enter your task's title: ")
        description = input("Enter your task's description: ")
        completed = False
        todo_list.add_task(title, description, completed)
        print(f"{title} task has been added!")
    elif op == 3:
        title = input("Enter your task's title: ")
        todo_list.remove_task(title)
        print(f"{title} task has been removed!")
    elif op == 4:
        todo_list.show_tasks()
        print("Tasklist was sorted successfully!")
    elif op == 5:
        title = input("Enter your task's title: ")
        todo_list.tick_task(title)
        print(f"{title} task has been done!")
    elif op == 6:
        start = False
        print("Session ended!")
    else:
        raise NotImplementedError