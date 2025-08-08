import streamlit as st
# 🎨 Background style
page_bg = '''
<style>
.stApp {
    background-image: url("https://unsplash.com/photos/vintage-teal-typewriter-beside-book-jLwVAUtLOAQ");
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
        if username == "Selva" and password == "1512":
            st.success("✅ Logged in successfully!")
            st.session_state.logged_in = True
            st.switch_page("pages/Home.py")  # ✅ Redirect after login
        else:
            st.error("❌ Invalid username or password.")
