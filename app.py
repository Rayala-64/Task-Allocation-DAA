import streamlit as st

st.set_page_config(page_title="DAA Task Allocation", layout="centered")

st.title("🤖 Task Allocation using DAA Algorithms")
st.markdown("""
Welcome to our **Design and Analysis of Algorithms (DAA)** project!

This application compares the performance of different algorithms for allocating tasks to servers based on CPU and Memory usage.

### 📌 Algorithms Included:
- Greedy
- Greedy Multi-Knapsack
- 1D Knapsack
- 2D Knapsack

Click the button below to get started!
""")

if st.button("🚀 Go to Main Page"):
    st.switch_page("pages/1_Main_Page.py")
    st.switch_page("pages/1_Summary.py")
