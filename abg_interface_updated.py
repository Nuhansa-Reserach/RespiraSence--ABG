import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(page_title="RespiraSence-ABG", page_icon="🩸", layout="centered")

# --- Blood Cell UI Header ---
st.markdown("""
    <div style='background-color:#ffe6e6;padding:20px;border-radius:10px;'>
        <h1 style='color:#800000;text-align:center;'>🩺 RespiraSence-ABG</h1>
        <h4 style='color:#660000;text-align:center;'>AI-Powered Blood Gas Interpretation for Modern Medicine</h4>
    </div>
""", unsafe_allow_html=True)

# --- Basic Login ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if email == "nuhansa@example.com" and password == "1234":
            st.success("Login successful!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid email or password.")
    st.stop()

# --- ABG Entry ---
st.subheader("🧪 Enter ABG Parameters")

pH = st.number_input("pH", value=7.40)
pCO2 = st.number_input("pCO₂ (mmHg)", value=40.0)
pO2 = st.number_input("pO₂ (mmHg)", value=90.0)
HCO3 = st.number_input("HCO₃ (mEq/L)", value=24.0)
SaO2 = st.number_input("SaO₂ (%)", value=98.0)

if st.button("🔍 Analyze ABG"):
    abnormal = pH < 7.35 or pH > 7.45 or pCO2 < 35 or pCO2 > 45 or pO2 < 75 or pO2 > 100 or HCO3 < 22 or HCO3 > 26 or SaO2 < 95

    if not abnormal:
        st.success("✅ ABG Status: Normal")
    else:
        st.error("⚠️ Status: Abnormal")
        st.markdown("### 🩺 Possible Symptoms:")
        st.markdown("""
        - Shortness of breath  
        - Dizziness or confusion  
        - Rapid breathing  
        - Fatigue or drowsiness  
        - Cyanosis (bluish lips or fingers)
        """)
        st.markdown("### 💡 Suggested Actions:")
        st.markdown("""
        - Repeat ABG test  
        - Administer oxygen  
        - Consult specialist  
        - Consider ICU monitoring
        """)

# Footer
st.markdown("---")
st.caption("Developed by **Nuhansa Herath** - BEng(Hons) in Biomedical Engineering Final Year Project - London Metropolitan University")

