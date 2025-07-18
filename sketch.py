# imagination-sketch/sketch.py
import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from huggingface_hub import login
from utils import save_image
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# Login to Hugging Face
if hf_token:
    login(hf_token)
else:
    st.error("Hugging Face token not found. Make sure .env is set properly.")

@st.cache_resource
def load_pipeline():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    return pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def show_sketch_page(username):
    st.subheader("Generate Your Imagination")
    pipe = load_pipeline()

    prompt = st.text_input("Enter a sketch idea (e.g., 'cat drinking milk')")
    if st.button("Generate"):
        with st.spinner("Generating your imagination..."):
            image = pipe(prompt).images[0]
            filename = save_image(image, prompt, username)
            st.image(image, caption="Your Sketch", use_column_width=True)
            st.success(f"Sketch saved as `{filename}`")
