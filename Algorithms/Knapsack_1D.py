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


def Knapsack(Tasks, CPU_Capacity):
    n = len(Tasks)
    values = [task["Priority"] for task in Tasks]
    weights = [task["CPU_Usage"] for task in Tasks]

    dp = [[0 for _ in range(CPU_Capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, CPU_Capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = CPU_Capacity
    selected_tasks = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_tasks.append(Tasks[i - 1])
            w -= weights[i - 1]

    selected_tasks.reverse()
    return selected_tasks


if __name__ == "__main__":
    cpu_capacity = int(input("Enter total CPU Capacity: "))
    tasks = get_tasks_from_user()

    selected = Knapsack(tasks, cpu_capacity)

    print("\nTasks Assigned to Server:")
    for task in selected:
        print(f"- Task ID {task['Task_ID']}: {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")

    used_cpu = sum(task["CPU_Usage"] for task in selected)
    print(f"\nTotal CPU Used: {used_cpu} / {cpu_capacity}")
    print(f"CPU Utilization: {round((used_cpu / cpu_capacity) * 100, 2)}%")







