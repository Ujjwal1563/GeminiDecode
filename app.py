from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Load environment variables from .env file
load_dotenv()

# Streamlit configuration
st.set_page_config(page_title="GeminiDecode:Multilanguage Document Extraction by Gemini Pro")

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Use the new model "gemini-1.5-flash"
    
    # Instead of converting the image to bytes, we pass the image directly as a PIL object
    response = model.generate_content([input, image, prompt])  # Pass image as PIL.Image.Image
    return response.text

# Streamlit UI components
st.header("GeminiDecode:Multilanguage Document Extraction by Gemini Pro")

text = """Utilizing Gemini Pro AI, this project effortlessly extracts vital information from diverse multilingual documents,
transcending language barriers with precision and efficiency for enhanced productivity and decision-making."""
styled_text = f"<span style='font-family:serif;'>{text}</span>"
st.markdown(styled_text, unsafe_allow_html=True)

# File uploader for image input
uploaded_file = st.file_uploader("Choose an image of the document:", type=["jpg", "jpeg", "png"])

image = None  # Initialize image variable

# Handle image upload
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Open image using PIL
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Input prompt for the model
input_prompts = """
You are expert in understanding invoices.
We will upload an image as an invoice, and you will have to answer any questions based on the uploaded invoice image.
"""

# Button to trigger model response
submit = st.button("Tell me about the document")

# Handle button click
if submit:
    if image:  # Check if an image was uploaded
        response = get_gemini_response(input_prompts, image, "Please analyze the uploaded invoice.")
        st.subheader("The response is:")
        st.write(response)
    else:
        st.error("Please upload an image first.")
