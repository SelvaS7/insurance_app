
import streamlit as st

st.set_page_config(page_title="Login", layout="centered")

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: purple;
    }
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 100px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='centered'><h1>🔐 Agent Login</h1></div>", unsafe_allow_html=True)

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.button("Login", type="primary"):
    if username == "selva" and password == "1410":
        st.session_state.logged_in = True
        st.success("Login successful! Redirecting...")
        st.switch_page("pages/Home.py")
    else:
        st.error("Invalid username or password")
