# imagination-sketch/user_history.py
import streamlit as st
from db_config import get_db
import os

def show_history_page(username):
    st.subheader(" Your Sketch History")
    db = get_db()
    items = db.history.find({"username": username}).sort("timestamp", -1)

    for item in items:
        st.markdown(f"**Prompt**: {item['prompt']}  \n {item['timestamp']}")
        image_path = os.path.join("static", "sketches", item["filename"])
        if os.path.exists(image_path):
            st.image(image_path, width=300)