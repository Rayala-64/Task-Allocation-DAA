import streamlit as st
from Algorithms.Greedy import greedy_allocation
from Algorithms.Greedy_MultiKnapsack import greedy_multi_knapsack
from Algorithms.Knapsack_1D import Knapsack
from Algorithms.Knapsack_2D import Knapsack2D
from Utils.metrics import calculate_cpu_utilization, calculate_memory_utilization

st.set_page_config(page_title="Main Allocation Page", layout="centered")
st.title("🧠 Task Allocation Engine")

# Select algorithm
algorithm = st.selectbox("Select Allocation Algorithm", [
    "Greedy", "Greedy Multi-Knapsack", "1D Knapsack", "2D Knapsack"
])

# Input CPU and optionally Memory
cpu_capacity = st.number_input("Enter Total CPU Capacity", min_value=1)
mem_capacity = None
if algorithm == "2D Knapsack":
    mem_capacity = st.number_input("Enter Total Memory Capacity", min_value=1)

# Task input
st.subheader("📝 Enter Task Details")
num_tasks = st.number_input("Number of Tasks", min_value=1, max_value=20, step=1)
tasks = []
for i in range(num_tasks):
    st.markdown(f"**Task {i+1}**")
    name = st.text_input(f"Task {i+1} Name", key=f"name{i}")
    cpu = st.number_input(f"CPU Usage", min_value=1, key=f"cpu{i}")
    priority = st.number_input(f"Priority", min_value=1, key=f"priority{i}")
    task = {"Task_ID": 100+i, "Task_Name": name, "CPU_Usage": cpu, "Priority": priority}
    if algorithm == "2D Knapsack":
        mem = st.number_input(f"Memory Usage", min_value=1, key=f"mem{i}")
        task["Memory_Usage"] = mem
    tasks.append(task)

# Server input (for Multi-Knapsack)
servers = []
if algorithm == "Greedy Multi-Knapsack":
    st.subheader("🖥️ Server Details")
    num_servers = st.number_input("Number of Servers", min_value=1, max_value=10, step=1)
    for i in range(num_servers):
        st.markdown(f"**Server {i+1}**")
        cap = st.number_input(f"CPU Capacity", min_value=1, key=f"serv{i}")
        servers.append({"Server_ID": 200+i, "CPU_Capacity": cap})

# Run the algorithm
if st.button("✅ Allocate Tasks"):
    if algorithm == "Greedy":
        selected = greedy_allocation(tasks, cpu_capacity)
        used, util = calculate_cpu_utilization(selected, cpu_capacity)

        st.success("✅ Task Allocation Completed")
        st.write("### Assigned Tasks")
        st.table(selected)
        st.markdown(f"**CPU Utilization:** {used} / {cpu_capacity} → **{util:.2f}%**")

    elif algorithm == "1D Knapsack":
        selected = Knapsack(tasks, cpu_capacity)
        used, util = calculate_cpu_utilization(selected, cpu_capacity)

        st.success("✅ Task Allocation Completed")
        st.write("### Assigned Tasks")
        st.table(selected)
        st.markdown(f"**CPU Utilization:** {used} / {cpu_capacity} → **{util:.2f}%**")

    elif algorithm == "2D Knapsack":
        selected = Knapsack2D(tasks, cpu_capacity, mem_capacity)
        used_cpu, util_cpu = calculate_cpu_utilization(selected, cpu_capacity)
        used_mem, util_mem = calculate_memory_utilization(selected, mem_capacity)

        st.success("✅ Task Allocation Completed")
        st.write("### Assigned Tasks")
        st.table(selected)
        st.markdown(f"**CPU Utilization:** {used_cpu}/{cpu_capacity} → **{util_cpu:.2f}%**")
        st.markdown(f"**Memory Utilization:** {used_mem}/{mem_capacity} → **{util_mem:.2f}%**")

    elif algorithm == "Greedy Multi-Knapsack":
        result = greedy_multi_knapsack(tasks, servers)
        total_used = 0
        total_capacity = sum(s["CPU_Capacity"] for s in servers)

        st.success("✅ Task Assignment to Servers Completed")
        for sid, task_list in result.items():
            st.write(f"### Server {sid} Assigned Tasks")
            st.table(task_list)
            used, _ = calculate_cpu_utilization(task_list, next(s["CPU_Capacity"] for s in servers if s["Server_ID"] == sid))
            total_used += used
        st.markdown(f"**Total CPU Utilization:** {total_used} / {total_capacity} → **{(total_used / total_capacity) * 100:.2f}%**")
