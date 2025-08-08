
import streamlit as st
import pandas as pd
import pickle

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

df = pd.read_csv("Social_Network_Ads.csv")
X = df[['Age', 'EstimatedSalary']]
X_scaled = scaler.transform(X)

df['Purchase_Probability'] = model.predict_proba(X_scaled)[:, 1]
top_leads = df.sort_values(by='Purchase_Probability', ascending=False).head(10)

st.set_page_config(page_title="Top Leads", layout="wide")
st.title("📋 Leadboard - Top 10 Customers Most Likely to Buy")
st.dataframe(top_leads[['Age', 'EstimatedSalary', 'Purchase_Probability']].round(2))

st.download_button(
    label="📥 Download Top Leads as CSV",
    data=top_leads.to_csv(index=False),
    file_name="top_leads.csv",
    mime="text/csv"
)
