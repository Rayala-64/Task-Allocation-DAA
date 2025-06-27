# 🤖 Task Allocation using DAA Algorithms

This project demonstrates how different **Design and Analysis of Algorithms (DAA)** strategies can be used to efficiently allocate tasks to servers based on their CPU and memory usage.

Developed as part of an academic project, this interactive web-based tool allows users to input task parameters and compare the performance of multiple algorithms.

---

## 📌 Algorithms Implemented

- **Greedy Algorithm**
- **Greedy Multi-Knapsack**
- **1D Knapsack (0/1)**
- **2D Knapsack (CPU + Memory constraints)**

---

## 🖥️ Project Structure

```bash
.
├── Algorithms/                 # Contains all implemented algorithms
│   ├── Greedy.py
│   ├── Greedy_MultiKnapsack.py
│   ├── Knapsack_1D.py
│   └── Knapsack_2D.py
│
├── Utils/                     # Helper modules
│   ├── input_utils.py         # Input formatting and generators
│   └── metrics.py             # Utilization and performance metrics
│
├── pages/                     # Streamlit pages
│   ├── 1_Main_Page.py         # Task input + output display
│   └── 2_Summary.py           # Comparison table of all algorithms
│
├── app.py                     # Home page of Streamlit app
├── compare.py                 # Optional: standalone comparison script
└── README.md                  # Project documentation
