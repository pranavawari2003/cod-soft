class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty!")

    def mark_completed(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                self.tasks[task_index - 1] += " - Completed"
                print("Task marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid task number!")

    def delete_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                del self.tasks[task_index - 1]
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid task number!")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = input("Enter the task number to mark as completed: ")
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = input("Enter the task number to delete: ")
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
