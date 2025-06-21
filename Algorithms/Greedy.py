def get_tasks_from_user():
    tasks = []
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        print(f"Task {i+1}:")
        name = input("  Task Name: ")
        cpu = int(input("  CPU Usage: "))
        priority = int(input("  Priority (higher means more important): "))
        task_id = 100 + i  # just assign IDs starting from 100
        tasks.append({"Task_ID": task_id, "Task_Name": name, "CPU_Usage": cpu, "Priority": priority})
    return tasks

def greedy_allocation(tasks, cpu_capacity):
    # Sort by Priority/CPU ratio (value per weight)
    tasks_sorted = sorted(tasks, key=lambda t: t["Priority"] / t["CPU_Usage"], reverse=True)

    selected = []
    used_cpu = 0

    for task in tasks_sorted:
        if used_cpu + task["CPU_Usage"] <= cpu_capacity:
            selected.append(task)
            used_cpu += task["CPU_Usage"]

    return selected

if __name__ == "__main__":
    cpu_capacity = int(input("Enter total CPU Capacity: "))
    tasks = get_tasks_from_user()

    selected = greedy_allocation(tasks, cpu_capacity)

    print("\nGreedy Assigned Tasks:")
    for task in selected:
        print(f"- Task ID {task['Task_ID']}: {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")

    used_cpu = sum(task["CPU_Usage"] for task in selected)
    print(f"\nTotal CPU Used: {used_cpu} / {cpu_capacity}")
    print(f"CPU Utilization: {round((used_cpu / cpu_capacity) * 100, 2)}%")
