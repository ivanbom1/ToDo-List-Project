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

todo_list.add_task("Do my HW", "French class homework", False)

todo_list.add_task("Laundry", "Do my laundry", False)

todo_list.add_task("Algebra", "Last assignment", False)

todo_list.show_tasks()

todo_list.tick_task("Algebra")

todo_list.show_tasks()