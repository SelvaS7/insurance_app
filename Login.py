import streamlit as st

# Set page config
st.set_page_config(page_title="Login", page_icon="🔒", layout="centered")

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login Form
st.title("🔐 Login")
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        if username == "Selva" and password == "0412":
            st.success("✅ Logged in successfully!")
            st.session_state.logged_in = True
            st.switch_page("pages/Home.py")  # ✅ Redirect after login
        else:
            st.error("❌ Invalid username or password.")
