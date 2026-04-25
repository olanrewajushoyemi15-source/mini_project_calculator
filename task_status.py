def mark_complete(tasks):
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to mark complete: "))
        found = False

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                found = True

                if task["completed"]:
                    print("Task marked as completed.")
                else:
                    print("Task marked as not completed.")
                break

        if not found:
            print("Task ID not found.")

    except ValueError:
        print("Invalid input. Enter a number.")

        def delete_task(tasks):
            if not tasks:
                print("No tasks to delete.")
            return

    try:
        task_id = int(input("Enter task ID to delete: "))
        found = False

        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                tasks.pop(i)
                print("Task deleted successfully.")
                found = True
                break

        if not found:
            print("Task ID not found.")

        # Reassign IDs
        for index, t in enumerate(tasks):
            t["id"] = index + 1

    except ValueError:
        print("Invalid input. Enter a number.")
