import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ✅ Page config
st.set_page_config(page_title="Login", layout="centered")

# 🎨 Background style
page_bg = '''
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1588776814546-a282f59b710f");
    background-size: cover;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# 🔄 Load animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

login_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jcikwtux.json")

# 🏷️ Title + Animation
st.title("🔐 Welcome to the Insurance Predictor App")
st.markdown("Please log in to continue.")
st_lottie(login_anim, height=200)

# 🧾 Login form
with st.form("login_form"):
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    login_btn = st.form_submit_button("Login")

    if login_btn:
        # 🔒 Simple hardcoded check (for demo use only!)
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("✅ Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

# 💅 Style tweaks
st.markdown("""
<style>
input {
    border: 1px solid #ccc;
    padding: 8px;
    border-radius: 6px;
    width: 100%;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)
