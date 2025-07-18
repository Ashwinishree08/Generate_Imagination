# imagination-sketch/auth.py
import streamlit as st
from db_config import get_db
import bcrypt

def get_current_user():
    return st.session_state.get("user")

def show_login_page():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        db = get_db()
        user = db.users.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode(), user["password"].encode() if isinstance(user["password"], str) else user["password"]):
            st.session_state.user = {"username": username}
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password")

    if st.button("Go to Signup"):
        st.session_state.page = "signup"
        st.rerun()

def show_signup_page():
    st.subheader("Signup")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")

    if st.button("Signup"):
        db = get_db()
        if db.users.find_one({"username": username}):
            st.error("Username already exists.")
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            db.users.insert_one({"username": username, "password": hashed})
            st.success("Account created! Please log in.")
            st.session_state.page = "login"
            st.rerun()


    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()


def logout():
    st.session_state.user = None
    st.session_state.page = "login"
    for key in list(st.session_state.keys()):
        del st.session_state[key]
