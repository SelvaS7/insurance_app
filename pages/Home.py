
import streamlit as st
import pickle
import numpy as np


page_bg_img = '''
<style>
.stApp {
background-image: url("https://unsplash.com/photos/brown-concrete-building-during-daytime-SzMR1Vcf5aw");
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

st.set_page_config(page_title="Prediction", layout="centered")
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("💡 Insurance Purchase Prediction Tool")

age = st.number_input("Enter Age", min_value=18, max_value=100, value=30)
salary = st.number_input("Enter Estimated Salary", min_value=0, max_value=10000000, value=50000)

if st.button("Predict"):
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
