import streamlit as st
import base64

## STREAMLIT CONFIGURATION
## --------------------------------------------------------------------------------##
st.set_page_config(
    page_title="Delhi Metro Accessibility", page_icon="🚇", layout="wide"
)

st.markdown(
    """
        <style>
            .ezrtsby2 {
                height: 0px;

            }
            .ea3mdgi5 {
                padding-bottom: 1rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            h1{
                padding: 2px;
                text-align: center;
            }
            .st-emotion-cache-y4bq5x {
                display: block;
            }   
            .exotz4b0 {
                padding: 2px;
                text-align: center;
                display: block;
            }
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {
                padding: 1rem;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

# Read the HTML file
with open(r"Images/Delhi Accessibility.html", "r") as file:
    html_string = file.read()

st.title("Delhi Metro Accessibility")
st.text("Accessibility to the nearest metro station in Delhi NCR")
st.components.v1.html(html_string, height=600, scrolling=False)
