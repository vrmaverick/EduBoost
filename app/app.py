import streamlit as st
import json
from image_summarisation import image_summarization_page
from image_colorisaiton import image_colorisation_page
from image_sum_using_blip2 import image_summarization_page2
from blog import blog , apply_custom_css

# Main function to handle navigation and display pages
def main():
    apply_custom_css()

    # Sidebar navigation for main pages
    st.sidebar.title("📚 Navigation")
    page = st.sidebar.selectbox("Select Page", ["🏠 Home", "✍️ Blog Interface", "📄 Image Summarisation" , "Image Colorisation"])

    # Home Page
    if page == "🏠 Home":
        st.title("🏠 Welcome to Edu-Boost")
        st.write("Explore our AI-powered education platform. Our services include:")
        st.write("- 📝 **Blog Section**: Read and manage insightful blogs.")
        st.write("- 📊 **Image Summarisation**: Automatically summarise images.")
        st.write("- 🎨 **Image Colorisation**: Add color to black-and-white images.")
        st.write("- 🖼️ **Image Generation**: Generate new images using AI.")
        st.write("- 🧮 **Touch-Based Calculator**: An interactive calculator for various needs.")

    # Blog Interface Page
    elif page == "✍️ Blog Interface":
        blog()
    elif page == "📄 Image Summarisation":
        image_summarization_page()
    elif page == "Image Colorisation":
        image_colorisation_page()

if __name__ == '__main__':
    main()
