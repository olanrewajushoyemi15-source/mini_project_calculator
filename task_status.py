def mark_complete(tasks):
    if not tasks:
        print("No tasks available. ")
        return

    try:
        task_id = int(input("Enter task ID to mark complete.. "))
        for task in tasks["id"] == task_id:
            task["completed"] = not task["completed. "]
            if task["completed"]:
                print("Task marked a completed")
            else:
                print("Task mark as not completed.. ")
                return
            print("TAsk ID not found.. ")
    except ValueError:
        print("Invlid input . Enter a number. ")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.. ")
        return

    try:
        task_id = int(input("Enter task ID to delete.. "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                task.pop(i)
                print("Task deleted Successfully.. ")

        # Reassign IDs
        for index, t in enumerate(tasks):
            t["id"] = index + 1
            return

            print("Task ID not found...")
    except ValueError:
        print("Invalid input. Enter a number. ")
