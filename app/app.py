import streamlit as st
from image_summarisation import image_summarization_page
from image_colorisaiton import image_colorisation_page
from blog import blog_page, apply_custom_css
from login import login_or_register, is_logged_in, get_current_page

# Initialize session state variables if not already set
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "🏠 Home"

# Function to handle logging out
def logout():
    # Set logged_in to False and reset the current page
    st.session_state.logged_in = False
    st.session_state.current_page = "🏠 Home"
    # Clear username
    if 'username' in st.session_state:
        del st.session_state['username']
    st.success("You have successfully logged out.")

# Main function to handle navigation and display pages
def main():
    apply_custom_css()

    # Check if the user is logged in
    if not is_logged_in():
        login_or_register()  # Show login/register form if not logged in
        return

    # If logged in, show navigation sidebar and main content
    with st.sidebar:
        st.title(f"Welcome, {st.session_state.get('username', 'User')}! 👋")
        st.session_state.current_page = st.selectbox(
            "Select Page",
            ["🏠 Home", "✍️ Blog Interface", "📄 Image Summarisation", "🎨 Image Colorisation"],
            index=["🏠 Home", "✍️ Blog Interface", "📄 Image Summarisation", "🎨 Image Colorisation"].index(st.session_state.current_page)
        )
        
        # Add a settings dropdown with a logout option
        st.markdown("## ⚙️ Settings")
        settings = st.selectbox(
            "Account Options", 
            ["Settings", "Logout"], 
            key="settings"
        )

        if settings == "Logout":
            logout()

    # Redirect to the appropriate page based on the selection
    if st.session_state.current_page == "🏠 Home":
        st.title("🏠 Welcome to Edu-Boost")
        st.write("Explore our AI-powered education platform. Our services include:")
        st.write("- 📝 **Blog Section**: Read and manage insightful blogs.")
        st.write("- 📊 **Image Summarisation**: Automatically summarise images.")
        st.write("- 🎨 **Image Colorisation**: Add color to black-and-white images.")
        st.write("- 🖼️ **Image Generation**: Generate new images using AI.")
        st.write("- 🧮 **Touch-Based Calculator**: An interactive calculator for various needs.")

    elif st.session_state.current_page == "✍️ Blog Interface":
        blog_page()

    elif st.session_state.current_page == "📄 Image Summarisation":
        image_summarization_page()

    elif st.session_state.current_page == "🎨 Image Colorisation":
        image_colorisation_page()

if __name__ == '__main__':
    main()
