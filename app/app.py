import streamlit as st
import json
<<<<<<< HEAD
from image_summarisation import image_summarization_page
from image_colorisaiton import image_colorisation_page
from image_sum_using_blip2 import image_summarization_page2
from blog import blog , apply_custom_css
=======
from datetime import datetime
from image_summarisation import image_summarization_page

BLOG_FILE = 'blogs.json'

# Load blogs from a JSON file
def load_blogs():
    try:
        with open(BLOG_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save blogs to a JSON file
def save_blogs(blogs):
    with open(BLOG_FILE, 'w') as file:
        json.dump(blogs, file, indent=4)

# Add a new blog
def add_blog(title, content, image_url=None):
    blogs = load_blogs()
    if any(blog['title'] == title for blog in blogs):
        st.error(f"Blog with title '{title}' already exists. Please use a different title.")
        return
    new_blog = {
        'title': title,
        'content': content,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'image_url': image_url or "",
        'likes': 0,
        'comments': []
    }
    blogs.append(new_blog)
    save_blogs(blogs)
    st.success(f"Blog '{title}' added successfully!")

# Edit an existing blog
def edit_blog(old_title, new_title, new_content, new_image_url=None):
    blogs = load_blogs()
    for blog in blogs:
        if blog['title'] == old_title:
            blog['title'] = new_title
            blog['content'] = new_content
            blog['image_url'] = new_image_url or blog.get('image_url', "")
            blog['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_blogs(blogs)
            st.success(f"Blog '{old_title}' updated to '{new_title}' successfully!")
            return
    st.error(f"Blog '{old_title}' not found.")

# Add a comment to a blog
def add_comment(blog_title, comment):
    blogs = load_blogs()
    for blog in blogs:
        if blog['title'] == blog_title:
            if 'comments' not in blog:
                blog['comments'] = []
            blog['comments'].append({
                'comment': comment,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            save_blogs(blogs)
            st.success("Comment added successfully!")
            return
    st.error(f"Blog '{blog_title}' not found.")

# Increment the likes for a blog
def like_blog(blog_title):
    blogs = load_blogs()
    for blog in blogs:
        if blog['title'] == blog_title:
            blog['likes'] = blog.get('likes', 0) + 1
            save_blogs(blogs)
            st.success("Blog liked successfully!")
            return
    st.error(f"Blog '{blog_title}' not found.")

# Display a blog with options for comments and likes
def display_blog(blog):
    st.write(f"### {blog['title']}")
    st.write(f"_{blog['date']}_")

    # Display image if available
    if blog.get('image_url'):
        st.image(blog['image_url'], caption="Blog Image", use_column_width=True)

    st.markdown(blog['content'])

    # Likes and Like Button
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"👍 {blog.get('likes', 0)} Likes")
    with col2:
        if st.button("Like this blog"):
            like_blog(blog['title'])
    
    # Comments Section
    st.subheader("💬 Comments")
    comments = blog.get('comments', [])
    if comments:
        for comment in comments:
            st.write(f"{comment['date']}: {comment['comment']}")
    else:
        st.write("No comments yet.")

    # Toggle Comment Form
    if 'show_comment_form' not in st.session_state:
        st.session_state['show_comment_form'] = False

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Add Comment", key=f"add_comment_{blog['title']}"):
            st.session_state['show_comment_form'] = True

    if st.session_state['show_comment_form']:
        new_comment = st.text_area("Add a comment", key=f"comment_{blog['title']}")
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("Submit Comment", key=f"submit_comment_{blog['title']}"):
                if new_comment:
                    add_comment(blog['title'], new_comment)
                    st.session_state['show_comment_form'] = False
                else:
                    st.error("Please enter a comment.")
        with col2:
            if st.button("Close Comment Form", key=f"close_comment_form_{blog['title']}"):
                st.session_state['show_comment_form'] = False

# Improved navigation and style with custom CSS
def apply_custom_css():
    st.markdown("""
        <style>
        .css-1d391kg { background-color: #f0f0f0; padding: 20px; } /* Background color */
        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 { color: #333; } /* Text color */
        .stButton { margin-top: 10px; } /* Button margin */
        .stTextInput, .stTextArea { margin-bottom: 10px; } /* Input field margin */
        .css-18e3th9 { display: flex; justify-content: space-between; align-items: center; } /* Align buttons in forms */
        </style>
    """, unsafe_allow_html=True)
>>>>>>> upstream/main

# Main function to handle navigation and display pages
def main():
    apply_custom_css()

    # Sidebar navigation for main pages
    st.sidebar.title("📚 Navigation")
<<<<<<< HEAD
    page = st.sidebar.selectbox("Select Page", ["🏠 Home", "✍️ Blog Interface", "📄 Image Summarisation" , "Image Colorisation"])
=======
    page = st.sidebar.selectbox("Select Page", ["🏠 Home", "✍️ Blog Interface", "📄 Image Summarisation"])
>>>>>>> upstream/main

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
<<<<<<< HEAD
        blog()
    elif page == "📄 Image Summarisation":
        image_summarization_page()
    elif page == "Image Colorisation":
        image_colorisation_page()
=======
        st.title("✍️ Blog Interface")

        # Show list of blogs
        blogs = load_blogs()
        if blogs:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader("📝 Blog List")
            with col2:
                if st.button("➕ Add New Blog"):
                    st.session_state['show_add_blog'] = True

            if 'show_add_blog' not in st.session_state:
                st.session_state['show_add_blog'] = False

            if st.session_state['show_add_blog']:
                st.subheader("➕ Add a New Blog")
                title = st.text_input("Blog Title", key="add_blog_title")
                content = st.text_area("Blog Content", height=200, key="add_blog_content")
                image_url = st.text_input("Image URL (optional)", key="add_blog_image_url")

                col1, col2 = st.columns([3, 1])
                with col1:
                    if st.button("Submit New Blog", key="submit_new_blog"):
                        if title and content:
                            add_blog(title, content, image_url)
                            st.session_state['show_add_blog'] = False
                        else:
                            st.error("Please fill both title and content.")
                with col2:
                    if st.button("Close Add Blog Form", key="close_add_form"):
                        st.session_state['show_add_blog'] = False

            blog_titles = [blog['title'] for blog in blogs]
            selected_blog = st.selectbox("Select a blog to view/edit", [""] + blog_titles, key="blog_select")

            if selected_blog:
                blog_to_view = next((b for b in blogs if b['title'] == selected_blog), None)
                if blog_to_view:
                    st.subheader("📄 View Blog")
                    display_blog(blog_to_view)

                    # Button to toggle edit options
                    col1, col2 = st.columns([3, 1])
                    with col2:
                        if st.button(f"🛠️ Edit '{selected_blog}'", key=f"edit_{selected_blog}"):
                            st.session_state['show_edit'] = selected_blog

                    if 'show_edit' not in st.session_state:
                        st.session_state['show_edit'] = False

                    if st.session_state['show_edit'] == selected_blog:
                        st.subheader(f"🛠️ Edit '{selected_blog}'")
                        new_title = st.text_input("New Blog Title", value=blog_to_view['title'], key="edit_blog_title")
                        new_content = st.text_area("New Content", value=blog_to_view['content'], height=200, key="edit_blog_content")
                        new_image_url = st.text_input("Image URL (optional)", value=blog_to_view.get('image_url', ""), key="edit_blog_image_url")

                        col1, col2 = st.columns([3, 1])
                        with col1:
                            if st.button("Update Blog", key=f"update_{selected_blog}"):
                                if new_title and new_content:
                                    edit_blog(blog_to_view['title'], new_title, new_content, new_image_url)
                                    st.session_state['show_edit'] = False  # Hide edit form after update
                                else:
                                    st.error("Please fill both title and content.")
                        with col2:
                            if st.button("Close Edit Form", key=f"close_edit_form_{selected_blog}"):
                                st.session_state['show_edit'] = False

        else:
            st.write("No blogs available.")

    # Image Summarisation
    elif page == "📄 Image Summarisation":
        image_summarization_page()
>>>>>>> upstream/main

if __name__ == '__main__':
    main()
