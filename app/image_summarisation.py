from PIL import Image
import io
import google.generativeai as genai
import streamlit as st
import json
import os
from datetime import datetime
<<<<<<< HEAD

# Set the Google API key
=======
>>>>>>> upstream/main
os.environ["GOOGLE_API_KEY"] = "AIzaSyCv1YBH9lmWj4Kd4559O-GpRTI-6V-6BtY"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
FEEDBACK_FILE = 'feedback.json'

def initialize_model():
    # Use environment variable for API key
<<<<<<< HEAD
    api_key = os.getenv('GOOGLE_API_KEY')
=======
    api_key = os.getenv('GENAI_API_KEY')
>>>>>>> upstream/main
    genai.api_key = api_key
    return genai.GenerativeModel('gemini-pro')

def read_image(image_file):
    # Convert the uploaded file to a PIL Image
    image = Image.open(image_file)
    return image

def image_to_byte_array(image):
    # No need for saving to a BytesIO object
    return image

def summarize_image(image_file, keywords):
    model = initialize_model()
    image = read_image(image_file)  # Convert to PIL Image
    image_content = image_to_byte_array(image)  # Convert to byte array

    try:
        response = model.generate_content(
            [
<<<<<<< HEAD
                f"Summarize this image {image_content} in an educational way. Here are some keywords to help you understand the context: {keywords}"
            ]
=======
                f"Summarize this image {image_content} in an educational way. Here are some keywords to help you understand the context: {keywords}"            ]
>>>>>>> upstream/main
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

<<<<<<< HEAD
def get_keywords(image_file, question, summary):
=======
def get_keywords(image_file, question):
>>>>>>> upstream/main
    model = initialize_model()
    image = read_image(image_file)  # Convert to PIL Image
    image_content = image_to_byte_array(image)  # Convert to byte array

    try:
        response = model.generate_content(
            [
<<<<<<< HEAD
                f"Answer the following question about this image, {image_content}: {question}",
                f'Here is the summary of the page: {summary}'
=======
                f"Answer the following question about this image , {image_content}: {question}",
                f'heres the summary of the page {summary}'
              
>>>>>>> upstream/main
            ]
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def handle_feedback(feedback):
    feedback_data = {
        'feedback': feedback,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as file:
            all_feedback = json.load(file)
    else:
        all_feedback = []

    all_feedback.append(feedback_data)
    
    with open(FEEDBACK_FILE, "w") as file:
        json.dump(all_feedback, file, indent=4)

def image_summarization_page():
    st.title("📷 Image Summarization")

<<<<<<< HEAD
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg" , "jfif" , "webp"])
=======
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
>>>>>>> upstream/main

    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        keywords = st.text_input("Enter keywords for summarization", "")

        if st.button("Generate Summary"):
            if uploaded_file and keywords:
<<<<<<< HEAD
                with st.spinner("🔍 Generating summary..."):
                    summary = summarize_image(uploaded_file, keywords)
                    st.session_state.summary = summary  # Store summary in session state
                    st.write("### Summary")
                    st.write(summary)
            else:
                st.error("Please upload an image and enter keywords.")

        # Display the stored summary if available
        if 'summary' in st.session_state:
            st.write("### Summary")
            st.write(st.session_state.summary)

        question = st.text_input("Ask a question about the image", "")
        if st.button("Get Answer"):
            if uploaded_file and question:
                with st.spinner("🤔 Getting answer..."):
                    answer = get_keywords(uploaded_file, question, st.session_state.summary)
                    st.write("### Answer")
                    st.write(answer)
=======
                summary = summarize_image(uploaded_file, keywords)
                st.write("### Summary")
                st.write(summary)
            else:
                st.error("Please upload an image and enter keywords.")

        question = st.text_input("Ask a question about the image", "")
        if st.button("Get Answer"):
            if uploaded_file and question:
                answer = get_keywords(uploaded_file, question)
                st.write("### Answer")
                st.write(answer)
>>>>>>> upstream/main
            else:
                st.error("Please upload an image and enter a question.")

        feedback = st.text_area("Provide feedback", "")
        if st.button("Submit Feedback"):
            if feedback:
                handle_feedback(feedback)
                st.success("Feedback submitted successfully!")
            else:
                st.error("Please enter your feedback.")
    else:
<<<<<<< HEAD
        st.write("Please upload an image to get started.")