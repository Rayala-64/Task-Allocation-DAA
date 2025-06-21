import time

def calculate_cpu_utilization(selected_tasks, total_cpu):
    used_cpu = sum(task["CPU_Usage"] for task in selected_tasks)
    utilization = (used_cpu / total_cpu) * 100 if total_cpu != 0 else 0
    return used_cpu, round(utilization, 2)

def calculate_memory_utilization(selected_tasks, total_memory):
    used_memory = sum(task.get("Memory_Usage", 0) for task in selected_tasks)
    utilization = (used_memory / total_memory) * 100 if total_memory != 0 else 0
    return used_memory, round(utilization, 2)

# ✅ Runtime measurement helper
def measure_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round((end_time - start_time) * 1000, 2)  # in milliseconds
        print(f"[RUNTIME] {func.__name__} took {runtime} ms")
        return result
    return wrapper

