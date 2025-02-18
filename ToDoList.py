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
            print(f"Title: {task.title}, Description: {task.description}, Completed: {task.completed}, Date: {task.date}")

    def add_task(self, title, description, completed=False):
        new_task = Task(title, description, completed)
        self.tasks.append(new_task)

todo_list = ToDoList()

todo_list.add_task("Do my HW", "French class homework", False)

todo_list.show_tasks()