import streamlit as st

st.set_page_config(page_title="Schema", page_icon=":sparkles:", layout="wide")
st.markdown("""
            <style>
                .block-container {
                        padding-top: 0rem;
                        padding-bottom: 2rem;   # this is to remove that blank space on top of the title 
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
            </style>
            """, unsafe_allow_html=True)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
        """
        <style>
        .center-title {
            font-size: 100px;
            font-weight: bold;
            text-align: center;
            color: #000000; /* Dark text color for title */
        }
        </style>
        <h1 class="center-title">✨ SCHEMA (TO-DO-LIST) ✨</h1>
        """, 
        unsafe_allow_html=True
    )

def main():

    st.title("My To-Do List 📃")  

    if 'todos' not in st.session_state:
        st.session_state.todos = []

    def add_todo():
        new_todo = st.session_state.new_todo.strip()  
        if new_todo:  
            st.session_state.todos.append({"task": new_todo, "done": False})
            st.session_state.new_todo = ""  

    
    st.text_input("Add a new task:", key="new_todo", on_change=add_todo)

   
    for index, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])  
        with col1:
            
            checkbox_key = f"checkbox_{index}"
            done = st.checkbox("", value=todo["done"], key=checkbox_key)
            st.session_state.todos[index]["done"] = done  
        with col2:
            
            if todo["done"]:
                st.markdown(f"<del>{todo['task']}</del>", unsafe_allow_html=True)
            else:
                st.info(todo["task"])
        with col3:
            
            if st.button("Delete", key=f"delete_{index}"):
                del st.session_state.todos[index]  
                st.rerun()  

    
    if st.session_state.todos:
        remaining_todos = sum(1 for todo in st.session_state.todos if not todo["done"])
        st.error(f"{remaining_todos} tasks remaining")
    else:
        st.info("You have no tasks yet. Add some!")

if __name__ == "__main__":
    main()  
