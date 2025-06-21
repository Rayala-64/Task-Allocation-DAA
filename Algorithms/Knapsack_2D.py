def get_tasks_from_user():
    tasks = []
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        print(f"Task {i+1}:")
        name = input("  Task Name: ")
        cpu = int(input("  CPU Usage: "))
        mem = int(input("  Memory Usage: "))
        priority = int(input("  Priority (higher means more important): "))
        task_id = 100 + i
        tasks.append({"Task_ID": task_id, "Task_Name": name, "CPU_Usage": cpu, "Memory_Usage": mem, "Priority": priority})
    return tasks

def Knapsack2D(tasks, cpu_capacity, mem_capacity):
    n = len(tasks)
    dp = [[[0] * (mem_capacity + 1) for _ in range(cpu_capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cpu = tasks[i - 1]["CPU_Usage"]
        mem = tasks[i - 1]["Memory_Usage"]
        value = tasks[i - 1]["Priority"]

        for c in range(cpu_capacity + 1):
            for m in range(mem_capacity + 1):
                if cpu <= c and mem <= m:
                    dp[i][c][m] = max(value + dp[i - 1][c - cpu][m - mem], dp[i - 1][c][m])
                else:
                    dp[i][c][m] = dp[i - 1][c][m]

    selected = []
    c, m = cpu_capacity, mem_capacity
    for i in range(n, 0, -1):
        if dp[i][c][m] != dp[i - 1][c][m]:
            selected.append(tasks[i - 1])
            c -= tasks[i - 1]["CPU_Usage"]
            m -= tasks[i - 1]["Memory_Usage"]

    selected.reverse()
    return selected

if __name__ == "__main__":
    cpu_capacity = int(input("Enter total CPU Capacity: "))
    mem_capacity = int(input("Enter total Memory Capacity: "))
    tasks = get_tasks_from_user()

    selected = Knapsack2D(tasks, cpu_capacity, mem_capacity)

    print("\nTasks Assigned to Server:")
    for task in selected:
        print(f"- Task ID {task['Task_ID']}: {task['Task_Name']} (CPU: {task['CPU_Usage']}, Memory: {task['Memory_Usage']}, Priority: {task['Priority']})")

    used_cpu = sum(task["CPU_Usage"] for task in selected)
    used_mem = sum(task["Memory_Usage"] for task in selected)

    print(f"\nCPU Used: {used_cpu} / {cpu_capacity}")
    print(f"Memory Used: {used_mem} / {mem_capacity}")
    print(f"CPU Utilization: {round((used_cpu / cpu_capacity) * 100, 2)}%")
    print(f"Memory Utilization: {round((used_mem / mem_capacity) * 100, 2)}%")
