import time
from Algorithms.Knapsack_1D import Knapsack
from Algorithms.Knapsack_2D import Knapsack2D
from Algorithms.Greedy import greedy_allocation
from Utils.metrics import calculate_cpu_utilization, calculate_memory_utilization
from Utils.input_utils import get_tasks_from_user

# Input section
cpu_capacity = int(input("Enter total CPU Capacity: "))
memory_capacity = int(input("Enter total Memory Capacity (for 2D only): "))

tasks = get_tasks_from_user(is_2d=True)

# Algorithm mapping
algorithms = {
    "1D Knapsack": Knapsack,
    "2D Knapsack": Knapsack2D,
    "Greedy": greedy_allocation
}

# Comparison Loop
for name, algo in algorithms.items():
    start = time.time()

    # Dynamically call the right function
    if name == "1D Knapsack":
        selected = algo(tasks, cpu_capacity)
    elif name == "2D Knapsack":
        selected = algo(tasks, cpu_capacity, memory_capacity)
    elif name == "Greedy":
        selected = algo(tasks, cpu_capacity)
    else:
        continue

    end = time.time()

    used_cpu, cpu_util = calculate_cpu_utilization(selected, cpu_capacity)
    print(f"\n{name} Algorithm:")
    print(f"→ Tasks Assigned: {len(selected)}")
    print(f"→ CPU Utilization: {cpu_util}%")

    # Memory Util for 2D
    if name == "2D Knapsack":
        used_mem, mem_util = calculate_memory_utilization(selected, memory_capacity)
        print(f"→ Memory Utilization: {mem_util}%")

    print(f"→ Time Taken: {round(end - start, 4)} seconds")
