import time
from Algorithms.Knapsack_1D import Knapsack
from Algorithms.Knapsack_2D import Knapsack2D
from Algorithms.Greedy import greedy_allocation
from Algorithms.Greedy_MultiKnapsack import greedy_multi_knapsack
from Utils.metrics import calculate_cpu_utilization, calculate_memory_utilization
from Utils.input_utils import get_tasks_from_user, get_servers_from_user
from tabulate import tabulate  # Add this at the top

# Input section
cpu_capacity = int(input("Enter total CPU Capacity: "))
memory_capacity = int(input("Enter total Memory Capacity (for 2D only): "))

# Collect tasks (set is_2d=True if you want memory input per task)
tasks = get_tasks_from_user(is_2d=True)

# Algorithm mapping
algorithms = {
    "1D Knapsack": Knapsack,
    "2D Knapsack": Knapsack2D,
    "Greedy": greedy_allocation,
    "Greedy Multi-Knapsack": greedy_multi_knapsack
}

# Summary list to hold results
summary = []

# Comparison Loop
for name, algo in algorithms.items():
    print(f"\n--- Running {name} ---")
    start = time.time()

    # Dynamically call the right function
    if name == "1D Knapsack":
        selected = algo(tasks, cpu_capacity)

        # Print result
        print("\nSelected Tasks:")
        for task in selected:
            print(f" - {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")

    elif name == "2D Knapsack":
        selected = algo(tasks, cpu_capacity, memory_capacity)

        print("\nSelected Tasks:")
        for task in selected:
            print(f" - {task['Task_Name']} (CPU: {task['CPU_Usage']}, Memory: {task['Memory_Usage']}, Priority: {task['Priority']})")

    elif name == "Greedy":
        selected = algo(tasks, cpu_capacity)

        print("\nSelected Tasks:")
        for task in selected:
            print(f" - {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")

    elif name == "Greedy Multi-Knapsack":
        servers = get_servers_from_user()
        selected = algo(tasks, servers)

        print("\nTask Assignment to Servers:")
        for sid, task_list in selected.items():
            print(f"\nServer {sid} assigned tasks:")
            for task in task_list:
                print(f"  - {task['Task_Name']} (CPU: {task['CPU_Usage']}, Priority: {task['Priority']})")

    else:
        continue

    end = time.time()
    runtime_ms = round((end - start) * 1000, 2)
    print(f"\n{name} completed in {runtime_ms} ms.")
    
    # Initialize summary row
    row = {
     "Algorithm": name,
     "Time (ms)": runtime_ms,
     "CPU Used": 0,
     "CPU Cap": 0,
     "CPU Util (%)": 0,
     "Memory Used": "-",
     "Memory Cap": "-",
     "Memory Util (%)": "-"
    }
    # Calculate CPU and Memory Utilization
    if name == "Greedy Multi-Knapsack":
        total_used_cpu = 0
        total_capacity = 0
        for server in servers:
            sid = server["Server_ID"]
            task_list = selected[sid]
            used_cpu, cpu_util = calculate_cpu_utilization(task_list, server["CPU_Capacity"])
            total_used_cpu += used_cpu
            total_capacity += server["CPU_Capacity"]
            print(f"Server {sid} CPU Utilization: {cpu_util:.2f}% (Used {used_cpu}/{server['CPU_Capacity']})")

        row["CPU Used"] = total_used_cpu
        row["CPU Cap"] = total_capacity
        row["CPU Util (%)"] = round((total_used_cpu / total_capacity) * 100, 2)
    
    else:
        used_cpu, cpu_util = calculate_cpu_utilization(selected, cpu_capacity)
        row["CPU Used"] = used_cpu
        row["CPU Cap"] = cpu_capacity
        row["CPU Util (%)"] = cpu_util
        print(f"Total CPU Utilization: {cpu_util:.2f}% (Used {used_cpu}/{cpu_capacity})")
        
        if name == "2D Knapsack":
            used_mem, mem_util = calculate_memory_utilization(selected, memory_capacity)
            row["Memory Used"] = used_mem
            row["Memory Cap"] = memory_capacity
            row["Memory Util (%)"] = mem_util
            print(f"Total Memory Utilization: {mem_util:.2f}% (Used {used_mem}/{memory_capacity})")

    summary.append(row)

# Print summary table
# After all algorithms processed
print("\n\n📊 Summary of All Algorithms:")
print(tabulate(summary, headers="keys", tablefmt="pretty"))