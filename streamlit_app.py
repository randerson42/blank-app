import streamlit as st
import requests

st.title("Pensive.AI \u00A0 🫐🍒")
st.header("Report Generator")
st.markdown("<br>", unsafe_allow_html=True)

Make_url = "https://hook.us2.make.com/aseggcntpt5uilz5091p7rrjno87ooyi"

# Columns to place buttons side by side
st.markdown("<br>", unsafe_allow_html=True)
phone = st.text_input("📱 Enter your phone number (+437241xxxx)")
query = st.text_input("Focus of Report? (blank if none)")
col1, col2 = st.columns(2)

report = None
timeframe = ""

# Button logic
with col1:
    if st.button("Daily Report"):
        # Insert daily summary logic here
        payload = {"phone": phone, "query": query, "time": "daily"}
        response = requests.post(Make_url, json=payload)
        report = response.text
        timeframe = "Daily"

with col2:
    if st.button("Weekly Report"):
        payload = {"phone": phone, "query": query, "time": "weekly"}
        response = requests.post(Make_url, json=payload)
        report = response.text
        timeframe = "Weekly"

if report:
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(timeframe +" " + "Pensive Report")
    st.write(report, unsafe_allow_html=True)
