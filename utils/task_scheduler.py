import streamlit as st

def schedule_tasks(tasks):
    # Sort tasks based on end time (greedy approach)
    tasks.sort(key=lambda x: x[1])
    selected = []
    last_end_time = 0

    for start, end in tasks:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end
    return selected

def run_task_scheduler_app():
    st.header("📅 Task Scheduler")
    st.markdown("""
    This tool schedules the **maximum number of non-overlapping tasks** based on start and end times.  
    Used in: employee scheduling, event planning, job/task queueing, etc.
    """)

    num_tasks = st.number_input("Number of Tasks", min_value=1, max_value=20, value=4)
    tasks = []

    st.subheader("🕓 Enter Task Timings")
    for i in range(num_tasks):
        col1, col2 = st.columns(2)
        with col1:
            start = st.number_input(f"Task {i+1} Start Time", key=f"start{i}")
        with col2:
            end = st.number_input(f"Task {i+1} End Time", key=f"end{i}")
        if start < end:
            tasks.append((start, end))

    if st.button("🧠 Schedule Tasks"):
        selected = schedule_tasks(tasks)
        st.success(f"✅ {len(selected)} Task(s) Scheduled Successfully!")
        for i, (start, end) in enumerate(selected,
