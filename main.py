import streamlit as st
from Todo import Todo
from datetime import datetime

st.set_page_config(page_title="Todo App", layout="centered")

st.title("✅ Todo App")

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = []

if "data_complete" not in st.session_state:
    st.session_state.data_complete = []

# Input for new task
new = st.text_input("Add a New Task", placeholder="Enter task here...")

if st.button("➕ Add Task"):
    if new.strip():
        new_todo = Todo(new.strip())
        st.session_state.data.append(new_todo)
        st.toast("✅ Task added successfully!", icon="🎉")
        st.rerun()
    else:
        st.warning("⚠️ Task cannot be empty!")

# **Pending Tasks**
st.subheader("📌 Pending Tasks")
if not st.session_state.data:
    st.info("🎯 No pending tasks!")
else:
    for index, item in enumerate(st.session_state.data):
        col1, col2, col3 = st.columns([4, 1, 1])
        col1.write(f"📝 {item.title}")
        if col2.button("✔️ Done", key=f"done{index}"):
            item.set_complete()
            item.set_complete()
            st.session_state.data.remove(item)
            st.session_state.data_complete.append(item)
            st.rerun()
        if col3.button("🗑️ Delete", key=f"delete{index}"):
            st.session_state.data.remove(item)
            st.rerun()

# **Completed Tasks**
st.subheader("✅ Completed Tasks")
if not st.session_state.data_complete:
    st.info("🎯 No completed tasks!")
else:
    for item in st.session_state.data_complete:
        col1, col2 = st.columns([3, 2])
        col1.write(f"✔️ {item.title}")
        col2.write(f"📅 {item.complete_at}")

    # Add a button to clear completed tasks
    if st.button("🗑️ Clear Completed Tasks"):
        st.session_state.data_complete.clear()
        st.success("All completed tasks removed!")
        st.rerun()
