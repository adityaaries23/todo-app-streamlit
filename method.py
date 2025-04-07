from Todo import Todo
import streamlit as st


def add_task(task: str):
    if task.strip():
        new_todo = Todo(task.strip())
        st.session_state.data.append(new_todo)
        st.toast("✅ Task added successfully!", icon="🎉")
        st.rerun()
    else:
        st.warning("⚠️ Task cannot be empty!")


def complete_task(todos, completed, index):
    todos[index].set_complete()
    completed.append(todos.pop(index))
    st.rerun()

def delete_task(todos, index):
    todos.pop(index)
    st.rerun()