def greedy_multi_knapsack(tasks, servers):
    tasks_sorted = sorted(tasks, key=lambda t: t["Priority"] / t["CPU_Usage"], reverse=True)

    assignment = {server["Server_ID"]: [] for server in servers}
    capacities = {server["Server_ID"]: server["CPU_Capacity"] for server in servers}

    for task in tasks_sorted:
        for server in servers:
            sid = server["Server_ID"]
            if capacities[sid] >= task["CPU_Usage"]:
                assignment[sid].append(task)
                capacities[sid] -= task["CPU_Usage"]
                break

    return assignment

def get_tasks_from_user():
    tasks = []
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        print(f"Task {i+1}:")
        name = input("  Task Name: ")
        cpu = int(input("  CPU Usage: "))
        priority = int(input("  Priority (higher means more important): "))
        task_id = 100 + i
        tasks.append({"Task_ID": task_id, "Task_Name": name, "CPU_Usage": cpu, "Priority": priority})
    return tasks

def get_servers_from_user():
    servers = []
    m = int(input("Enter number of servers: "))
    for i in range(m):
        print(f"Server {i+1}:")
        capacity = int(input("  CPU Capacity: "))
        server_id = 200 + i
        servers.append({"Server_ID": server_id, "CPU_Capacity": capacity})
    return servers

# Run the complete assignment
if __name__ == "__main__":
    tasks = get_tasks_from_user()
    servers = get_servers_from_user()
    result = greedy_multi_knapsack(tasks, servers)

    print("\nTask Assignment to Servers:")
    for sid, task_list in result.items():
        print(f"\nServer {sid} assigned tasks:")
        for task in task_list:
            print(f"  - {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")
