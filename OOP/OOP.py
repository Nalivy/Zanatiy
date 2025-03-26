class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title}"

class TaskManager:
    def __init__(self):
        self.taski = []

    def add_task(self, title):
        task = Task(title)
        self.taski.append(title)

    def remove_task(self, title):
        self.taski =[task for task in self.taski if task.title != title]