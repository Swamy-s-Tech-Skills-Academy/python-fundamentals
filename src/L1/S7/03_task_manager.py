# Filename: src/L1/S7/03_task_manager.py

"""
📋 Simple Task Manager
Demonstrates lists and loops working together!
"""

print("=" * 50)
print("📋 SIMPLE TASK MANAGER")
print("=" * 50)

tasks = []

while True:
    print("\n--- Menu ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Remove task")
    print("5. Quit")

    choice = input("\nEnter choice (1-5): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"✅ Added: '{task}'")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks yet!")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("📭 No tasks to complete!")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

            try:
                num = int(input("Enter task number to complete: "))
                if 1 <= num <= len(tasks):
                    completed = tasks.pop(num - 1)
                    print(f"🎉 Completed: '{completed}'")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("❌ Please enter a number!")

    elif choice == "4":
        if len(tasks) == 0:
            print("📭 No tasks to remove!")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"🗑️ Removed: '{removed}'")
                else:
                    print("❌ Invalid task number!")
            except ValueError:
                print("❌ Please enter a number!")

    elif choice == "5":
        print("\n" + "=" * 50)
        print("👋 Goodbye! Stay productive!")
        print("=" * 50)
        break

    else:
        print("❌ Invalid choice! Please enter 1-5.")
