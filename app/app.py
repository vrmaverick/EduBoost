import streamlit as st
import json
from datetime import datetime
BLOG_FILE = 'blogs.json'

# Function to load blogs from a JSON file
def load_blogs():
    try:
        with open(BLOG_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save blogs to a JSON file
def save_blogs(blogs):
    with open(BLOG_FILE, 'w') as file:
        json.dump(blogs, file)
def add_blog(title, content):
    blogs = load_blogs()
    new_blog = {
        'title': title,
        'content': content,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    blogs.append(new_blog)
    save_blogs(blogs)
def display_blog(blog):
    st.write(f"### {blog['title']}")
    st.write(f"_{blog['date']}_")
    st.write(blog['content'])
def main():
    st.title("Simple Blogging Platform")

    # Sidebar for blog navigation and adding new blog entries
    st.sidebar.title("Navigation")
    menu = ["Home", "Add Blog"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("All Blogs")
        blogs = load_blogs()
        
        if blogs:
            # Show list of blogs
            titles = [blog['title'] for blog in blogs]
            selected_blog = st.sidebar.selectbox("Select a blog", titles)
            blog = next((b for b in blogs if b['title'] == selected_blog), None)
            if blog:
                display_blog(blog)
        else:
            st.write("No blogs available.")

    elif choice == "Add Blog":
        st.subheader("Add a New Blog")
        title = st.text_input("Blog Title")
        content = st.text_area("Content", height=200)
        
        if st.button("Add Blog"):
            if title and content:
                add_blog(title, content)
                st.success(f"Blog '{title}' added successfully!")
            else:
                st.error("Please enter both a title and content.")

if __name__ == '__main__':
    main()
