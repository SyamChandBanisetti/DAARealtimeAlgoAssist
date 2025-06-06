# utils/scheduler.py

import streamlit as st
import matplotlib.pyplot as plt

def schedule_tasks(tasks):
    tasks.sort(key=lambda x: x[1])  # Sort by end time
    selected = []
    last_end_time = 0

    for start, end in tasks:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end
    return selected

def plot_schedule(tasks, selected):
    fig, ax = plt.subplots(figsize=(10, 2))
    y = 0.5
    height = 0.3
    for i, (start, end) in enumerate(tasks):
        color = 'green' if (start, end) in selected else 'gray'
        ax.barh(y, end - start, left=start, height=height, color=color, edgecolor='black')
        ax.text(start + (end - start) / 2, y, f'Task {i+1}', ha='center', va='center', color='white', fontsize=8)
    ax.set_xlabel('Time')
    ax.set_yticks([])
    ax.set_title('Task Schedule Timeline')
    ax.set_xlim(left=0)
    ax.grid(True, axis='x', linestyle='--', linewidth=0.5)
    return fig

def run_scheduler_app():
    st.set_page_config(page_title="Task Scheduler", layout="wide")

    st.sidebar.title("📘 User Guide")
    st.sidebar.markdown("""
    ### How to Use:
    1. **Select number of tasks** using the slider.
    2. **Input start and end times** for each task.
       - End time must be greater than start time.
    3. Click **🧠 Schedule Optimally** to see results.

    ### Output:
    - ✅ List of scheduled (non-overlapping) tasks.
    - 📊 Visual timeline of tasks (green = scheduled).

    ### Tips:
    - Use decimal values (e.g., 3.5) for precise timing.
    - Overlapping tasks are skipped automatically.
    """)

    st.title("📅 Smart Task Scheduler")
    st.markdown("""
    Schedule the **maximum number of non-overlapping tasks** efficiently.  
    Useful in: **job scheduling**, **event planning**, **task queueing**, and more.
    """)

    num_tasks = st.slider("🧮 Number of Tasks", min_value=1, max_value=15, value=4)
    tasks = []

    st.subheader("🕓 Task Timings")
    for i in range(num_tasks):
        with st.expander(f"📝 Task {i+1}"):
            col1, col2 = st.columns(2)
            with col1:
                start = st.number_input(f"Start Time for Task {i+1}", key=f"start{i}", format="%.2f")
            with col2:
                end = st.number_input(f"End Time for Task {i+1}", key=f"end{i}", format="%.2f")
            if start < end:
                tasks.append((start, end))
            else:
                st.warning(f"⚠️ Task {i+1}: End time must be greater than start time.")

    if st.button("🧠 Schedule Optimally"):
        if not tasks:
            st.error("❌ No valid tasks to schedule.")
            return

        selected = schedule_tasks(tasks)
        st.success(f"✅ {len(selected)} Task(s) Scheduled Successfully!")

        st.markdown("### 🗓️ Scheduled Tasks:")
        for i, (start, end) in enumerate(selected, 1):
            st.write(f"• Task {i}: Start = {start}, End = {end}")

        st.markdown("### 📊 Visual Task Timeline")
        fig = plot_schedule(tasks, selected)
        st.pyplot(fig)
