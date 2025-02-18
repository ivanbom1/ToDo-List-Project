class Task:
    def __init__(self, title, description, completed=False, date=None):
        self.title = title
        self.description = description
        self.completed = completed
        self.date = date
