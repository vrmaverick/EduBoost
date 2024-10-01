import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase app with service account credentials
def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("/workspace/EduBoost/Sign/eduboost-8850a-7e7039f83f3f.json")
        firebase_admin.initialize_app(cred)

# Register a new user with username
def register_user(username, email, password):
    try:
        user = auth.create_user(email=email, password=password)
        # Store user data in Firestore
        db = firestore.client()
        db.collection('users').document(user.uid).set({
            'username': username,
            'email': email
        })
        st.success(f"User {username} created successfully")
    except Exception as e:
        st.error(f"Error creating user: {e}")

# Sign in a user
def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # Simulating password verification - ideally use Firebase client-side for password validation
        st.success(f"Welcome, {user.display_name or email}! 👋")
        st.session_state.logged_in = True
        st.session_state.username = user.display_name or email  # Use username if available
        st.session_state.current_page = "🏠 Home"  # Set to home page after login
        st.rerun()  # Force rerun to refresh the page after login
    except Exception as e:
        st.error(f"Error logging in: {e}")

# Send password reset email
def send_password_reset_email(email):
    try:
        auth.send_password_reset_email(email)
        st.success(f"Password reset email sent to {email}. Please check your inbox.")
    except Exception as e:
        st.error(f"Error sending password reset email: {e}")

# Function to check if user is logged in
def is_logged_in():
    return st.session_state.get("logged_in", False)

# Login or registration UI
def login_or_register():
    st.title("🔒 Login or Register")
    action = st.radio("Choose Action", ("Login", "Register"))

    if action == "Login":
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            login_user(email, password)

        # Forgot Password Section
        if st.button("Forgot Password?"):
            email = st.text_input("Enter your email for password reset")
            if email and st.button("Send Reset Email"):
                send_password_reset_email(email)

    elif action == "Register":
        username = st.text_input("Username")  # Add username input
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            if username and email and password:  # Ensure all fields are filled
                register_user(username, email, password)
            else:
                st.error("Please fill in all fields.")

# Call the init_firebase function to initialize Firebase
init_firebase()

# Initialize user session state if not already done
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'users' not in st.session_state:
    st.session_state.users = {}

# Display welcome message if logged i

def get_current_page():
    return st.session_state.get("current_page", "🏠 Home")
