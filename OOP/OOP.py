import json

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
        self.tasks = []
        self.load_from_file()

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def delete_task(self, nomer):
            if 1 <= nomer <= len(self.tasks):
                removed_task = self.tasks.pop(nomer - 1)
                print(f'Задача "{removed_task.title}" удалена.')
            else:
                print("Ошибка: Неверный номер задачи.")


    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст")
        else:
            for index,task in enumerate(self.tasks, start=1):
                print(f"{index}, {task}")

    def mark_task_completed(self, nomer):
            if 1 <= nomer <= len(self.tasks):
                task = self.tasks[nomer - 1]
                task.mark_completed()
                print(f'Задача "{task.title}" отмечена как выполненная.')
            else:
                print("Ошибка: Неверный номер задачи.")


    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task.title.lower()]

        if found_tasks:
            print("\nНайденные задачи:")
            for index, task in enumerate(found_tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Задачи не найдены.")

    def filter_tasks(self, completed=True):
        filtered_tasks = [task for task in self.tasks if task.completed == completed]

        if not filtered_tasks:
            status = "выполненных" if completed else "невыполненных"
            print(f"Нет {status} задач.")
            return

        print("Список задач:")
        for index, task in enumerate(filtered_tasks, start=1):
            print(f"{index}. {task}")

    def save_to_file(self, filename="tasks.json"):
        """Сохраняет список задач в JSON-файл."""
        data = [{"title": task.title, "completed": task.completed} for task in self.tasks]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("✅ Задачи сохранены в файл!")

    def load_from_file(self, filename="tasks.json"):
        """Загружает задачи из JSON-файла."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            self.tasks = [Task(item["title"]) for item in data]
            for task, item in zip(self.tasks, data):
                task.completed = item["completed"]

            print("📂 Задачи загружены из файла!")

        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ Файл не найден или пуст. Начинаем с нуля.")

def main():
    manager = TaskManager()

    while True:
        print("\n📌 Меню управления задачами:")
        print("1️⃣ Добавить задачу")
        print("2️⃣ Показать все задачи")
        print("3️⃣ Отметить задачу выполненной")
        print("4️⃣ Удалить задачу")
        print("5️⃣ Поиск задач")
        print("6️⃣ Показать выполненные задачи")
        print("7️⃣ Показать невыполненные задачи")
        print("8️⃣ Сохранить задачи")
        print("9️⃣ Выйти")

        choice = input("🔹 Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            manager.add_task(title)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            task_num = int(input("Введите номер задачи: "))
            manager.mark_task_completed(task_num)

        elif choice == "4":
            task_num = int(input("Введите номер задачи: "))
            manager.delete_task(task_num)

        elif choice == "5":
            keyword = input("Введите слово для поиска: ")
            manager.search_tasks(keyword)

        elif choice == "6":
            manager.filter_tasks(completed=True)

        elif choice == "7":
            manager.filter_tasks(completed=False)

        elif choice == "8":
            manager.save_to_file()

        elif choice == "9":
            print("👋 Выход из программы...")
            manager.save_to_file()
            break

        else:
            print("❌ Ошибка: некорректный ввод!")


if __name__ == "__main__":
    main()