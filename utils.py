# imagination-sketch/utils.py
import os
from PIL import Image
from datetime import datetime
from db_config import get_db

def save_image(image, prompt, username):
    os.makedirs("static/sketches", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{username}_{timestamp}.png"
    filepath = os.path.join("static", "sketches", filename)

    image.save(filepath)

    db = get_db()
    db.history.insert_one({
        "username": username,
        "prompt": prompt,
        "filename": filename,
        "timestamp": timestamp
    })

    return filename
