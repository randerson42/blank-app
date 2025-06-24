import streamlit as st
import requests

st.title("Pensive.AI ")
st.title("🍒🍎🫐")

Make_url = "https://hook.us2.make.com/aseggcntpt5uilz5091p7rrjno87ooyi"

# Columns to place buttons side by side
st.markdown("<br>", unsafe_allow_html=True)
phone = st.text_input("📱 Enter your phone number (+437241xxxx)")
query = st.text_input("Focus of Report? (blank if none)")
col1, col2 = st.columns(2)

# Button logic
with col1:
    if st.button("Daily Report"):
        # Insert daily summary logic here
        payload = {"phone": phone, "query": query, "source": "streamlit"}
        response = requests.post(Make_url, json=payload)
        st.write(response.text, unsafe_allow_html=True)

with col2:
    if st.button("Weekly Report"):
        st.write(f"🗓️ You clicked Weekly Summary for:")
        # Insert weekly summary logic here
