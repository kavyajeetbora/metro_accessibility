import streamlit as st

# Read the HTML file
with open(r"Images\Delhi Accessibility.html", "r") as file:
    html_string = file.read()

# Render the HTML content
st.markdown(html_string, unsafe_allow_html=True)
