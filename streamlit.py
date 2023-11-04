import streamlit as st
import Retreive as rt


def home():
    st.title("Welcome to Inscribd")
    # Add content for the home page
# Page 2: Lectures


def lectures():
    st.title("Lectures")
    st.markdown("## Transcription")
    st.write(rt.get_latest_file_content())


# Sidebar navigation
pages = {
    "Home": home,
    "Lectures": lectures,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
