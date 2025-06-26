def get_tasks_from_user(is_2d=False):
    tasks = []
    n = int(input("Enter number of tasks: "))
    for i in range(n):
        print(f"Task {i+1}:")
        name = input("  Task Name: ")
        cpu = int(input("  CPU Usage: "))
        priority = int(input("  Priority (higher means more important): "))
        task_id = 100 + i

        task = {"Task_ID": task_id, "Task_Name": name, "CPU_Usage": cpu, "Priority": priority}
        if is_2d:
            mem = int(input("  Memory Usage: "))
            task["Memory_Usage"] = mem

        tasks.append(task)
    return tasks

def get_servers_from_user():
    servers = []
    m = int(input("Enter number of servers: "))
    for i in range(m):
        print(f"Server {i+1}:")
        capacity = int(input("  CPU Capacity: "))
        servers.append({"Server_ID": 200 + i, "CPU_Capacity": capacity})
    return servers