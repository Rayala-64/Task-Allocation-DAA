import streamlit as st
import time
import pandas as pd

from Algorithms.Knapsack_1D import Knapsack
from Algorithms.Knapsack_2D import Knapsack2D
from Algorithms.Greedy import greedy_allocation
from Algorithms.Greedy_MultiKnapsack import greedy_multi_knapsack
from Utils.metrics import calculate_cpu_utilization, calculate_memory_utilization

st.set_page_config(page_title="Summary", layout="centered")
st.title("📊 Summary of All Algorithms")

# CPU and memory input
cpu_capacity = st.number_input("Enter total CPU Capacity", min_value=1)
memory_capacity = st.number_input("Enter total Memory Capacity (for 2D only)", min_value=0)

# Tasks input
st.subheader("📝 Enter Task Details")
num_tasks = st.number_input("Number of Tasks", min_value=1, max_value=20, step=1)
tasks = []
for i in range(num_tasks):
    st.markdown(f"**Task {i+1}**")
    name = st.text_input(f"Task {i+1} Name", key=f"name{i}")
    cpu = st.number_input(f"CPU Usage", min_value=1, key=f"cpu{i}")
    priority = st.number_input(f"Priority", min_value=1, key=f"priority{i}")
    task = {"Task_ID": 100+i, "Task_Name": name, "CPU_Usage": cpu, "Priority": priority}
    mem = st.number_input(f"Memory Usage (for 2D Knapsack)", min_value=0, key=f"mem{i}")
    task["Memory_Usage"] = mem
    tasks.append(task)

# Server input (for Multi-Knapsack)
st.subheader("🖥️ Server Details (for Multi-Knapsack)")
num_servers = st.number_input("Number of Servers", min_value=1, max_value=5, step=1)
servers = []
for i in range(num_servers):
    st.markdown(f"**Server {i+1}**")
    cap = st.number_input(f"CPU Capacity", min_value=1, key=f"server{i}")
    servers.append({"Server_ID": 200+i, "CPU_Capacity": cap})

# Run on click
if st.button("🔍 Compare All Algorithms"):
    summary = []

    for name in ["1D Knapsack", "2D Knapsack", "Greedy", "Greedy Multi-Knapsack"]:
        st.write(f"Running **{name}**...")
        start = time.time()

        if name == "1D Knapsack":
            selected = Knapsack(tasks, cpu_capacity)

        elif name == "2D Knapsack":
            selected = Knapsack2D(tasks, cpu_capacity, memory_capacity)

        elif name == "Greedy":
            selected = greedy_allocation(tasks, cpu_capacity)

        elif name == "Greedy Multi-Knapsack":
            selected = greedy_multi_knapsack(tasks, servers)

        else:
            continue

        end = time.time()
        runtime_ms = round((end - start) * 1000, 2)

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

        if name == "Greedy Multi-Knapsack":
            total_used_cpu = 0
            total_capacity = 0
            for server in servers:
                sid = server["Server_ID"]
                task_list = selected[sid]
                used_cpu, _ = calculate_cpu_utilization(task_list, server["CPU_Capacity"])
                total_used_cpu += used_cpu
                total_capacity += server["CPU_Capacity"]
            row["CPU Used"] = total_used_cpu
            row["CPU Cap"] = total_capacity
            row["CPU Util (%)"] = round((total_used_cpu / total_capacity) * 100, 2)

        else:
            used_cpu, cpu_util = calculate_cpu_utilization(selected, cpu_capacity)
            row["CPU Used"] = used_cpu
            row["CPU Cap"] = cpu_capacity
            row["CPU Util (%)"] = cpu_util

            if name == "2D Knapsack":
                used_mem, mem_util = calculate_memory_utilization(selected, memory_capacity)
                row["Memory Used"] = used_mem
                row["Memory Cap"] = memory_capacity
                row["Memory Util (%)"] = mem_util

        summary.append(row)

    # Display table
    st.success("✅ All algorithms evaluated!")
    df_summary = pd.DataFrame(summary)
    st.dataframe(df_summary, use_container_width=True)
