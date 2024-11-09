from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

load_dotenv()

st.set_page_config(page_title="GeminiDecode:Multilanguage Document Extraction by Gemini Pro")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image, prompt])  
    return response.text

st.header("GeminiDecode:Multilanguage Document Extraction by Gemini Pro")

text = """Utilizing Gemini Pro AI, this project effortlessly extracts vital information from diverse multilingual documents,
transcending language barriers with precision and efficiency for enhanced productivity and decision-making."""
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

image = None  

if uploaded_file is not None:
    image = Image.open(uploaded_file)  
    st.image(image, caption="Uploaded Image", use_column_width=True)

input_prompts = """
You are expert in understanding invoices.
We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
"""

submit = st.button("Tell me about the document")

if submit:
    if image:  
        response = get_gemini_response(input_prompts, image, "Please analyze the uploaded invoice.")
        st.subheader("The response is:")
        st.write(response)
    else:
        st.error("Please upload an image first.")
