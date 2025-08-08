import streamlit as st
import pickle
import numpy as np
from streamlit_lottie import st_lottie
import requests

# 🚫 Require login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

# ✅ Page config
st.set_page_config(page_title="Insurance Predictor", layout="centered")

# 🎨 Custom background
page_bg = '''
<style>
.stApp {
    background-image: url("https://unsplash.com/photos/brown-concrete-building-during-daytime-SzMR1Vcf5aw");
    background-size: cover;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

# 🔄 Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets5.lottiefiles.com/packages/lf20_x62chJ.json"  # You can replace with another
animation = load_lottieurl(lottie_url)

# 🧠 Load ML model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# 📝 Title and Animation
st.title("🛡️ Insurance Purchase Predictor")
st_lottie(animation, height=200, key="insurance_anim")

st.markdown("Use this tool to predict whether a customer is likely to purchase insurance based on age and salary.")

# 🧾 User Input
age = st.number_input("🎂 Enter Age", min_value=18, max_value=100, value=30)
salary = st.number_input("💰 Enter Estimated Salary", min_value=0, max_value=10000000, value=50000)

# 🔍 Predict
if st.button("🔮 Predict"):
    input_data = np.array([[age, salary]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("🎯 Prediction Result")
    if prediction == 1:
        st.success("✅ Likely to purchase insurance.")
    else:
        st.error("❌ Unlikely to purchase insurance.")

    st.subheader("📊 Confidence Level")
    st.metric("Probability", f"{probability * 100:.2f}%")
    st.progress(int(probability * 100))

# 📬 Contact Form
st.markdown("---")
st.markdown("### 📬 Contact Selvakumar")

contact_form = f"""
<form action="https://formsubmit.co/sk.selvakumar379@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# 👇 Styling for the contact form
st.markdown("""
<style>
input, textarea {
    width: 100%;
    padding: 8px;
    margin: 5px 0 10px 0;
    border: 1px solid #ccc;
    border-radius: 6px;
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
