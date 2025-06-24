import streamlit as st
import requests

st.title("Pensive.AI 🍒🍎🫐 - Report Generator")

Make_url = "https://hook.us2.make.com/aseggcntpt5uilz5091p7rrjno87ooyi"

# Columns to place buttons side by side
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

# Button logic
with col1:
    if st.button("Daily Report"):
        st.write(f"📅 You clicked Daily Summary for:")
        # Insert daily summary logic here
        payload = {"message": "test", "source": "streamlit"}
        response = requests.post(Make_url, json=payload)

with col2:
    if st.button("Weekly Report"):
        st.write(f"🗓️ You clicked Weekly Summary for: '{user_input}'")
        # Insert weekly summary logic here

# Text input
user_input = st.text_input("Specific Query Report:")

# Optional debug output
st.markdown("<br>", unsafe_allow_html=True)
st.write("Report:", user_input)
