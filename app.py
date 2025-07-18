# imagination-sketch/app.py
import streamlit as st
from auth import show_login_page, show_signup_page, get_current_user, logout
from sketch import show_sketch_page
from user_history import show_history_page

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Imagination Sketch", layout="centered")
    load_css()

    if "page" not in st.session_state:
        st.session_state.page = "login"

    st.markdown("<div class='main-title'>Imagination Sketch</div>", unsafe_allow_html=True)

    user = get_current_user()

    if user:
        menu = st.sidebar.selectbox("Menu", ["Generate Sketch", "My History", "Logout"])
        st.sidebar.markdown(f"Logged in as: `{user['username']}`")

        if menu == "Generate Sketch":
            show_sketch_page(user["username"])
        elif menu == "My History":
            show_history_page(user["username"])
        elif menu == "Logout":
            logout()
            st.rerun()

    else:
        if st.session_state.page == "login":
            show_login_page()
        else:
            show_signup_page()

if __name__ == "__main__":
    main()
