import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, description, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "priority": priority,
            "completed": False,
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        print(f"Task added: {description}")
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\n=== YOUR TASKS ===")
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            print(f"{status} [{task['id']}] {task['description']} ({task['priority']}) - {task['created']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"\nTask {task_id} marked as completed!")
                self.save_tasks()
                return
        print("\nTask not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        print(f"\nTask {task_id} deleted!")
        self.save_tasks()

    def save_tasks(self):
        try:
            with open("tasks.txt", "w") as file:
                for task in self.tasks:
                    file.write(f"{task['id']},{task['description']},{task['priority']},{task['completed']},{task['created']}\n")
        except Exception as e:
            print(f"\nError saving tasks: {e}")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 5:
                        task = {
                            "id": int(parts[0]),
                            "description": parts[1],
                            "priority": parts[2],
                            "completed": parts[3] == "True",
                            "created": parts[4]
                        }
                        self.tasks.append(task)
        except FileNotFoundError:
            print("\nNo existing tasks found. Starting fresh!")
        except Exception as e:
            print(f"\nError loading tasks: {e}")

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        try:
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                description = input("Enter task description: ")
                priority = input("Enter priority (high/medium/low): ").lower()
                if priority not in ["high", "medium", "low"]:
                    priority = "medium"
                manager.add_task(description, priority)
                
            elif choice == "2":
                manager.list_tasks()
                
            elif choice == "3":
                manager.list_tasks()
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    manager.complete_task(task_id)
                except ValueError:
                    print("\nPlease enter a valid task ID!")
                    
            elif choice == "4":
                manager.list_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    manager.delete_task(task_id)
                except ValueError:
                    print("\nPlease enter a valid task ID!")
                    
            elif choice == "5":
                print("\nGoodbye!")
                break
                
            else:
                print("\nInvalid choice! Please enter a number between 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()