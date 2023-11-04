import streamlit as st
from pymongo import MongoClient
uri = "mongodb+srv://shriteqhackathon:5F5RZ96CiqZY4jzM@hackathon.vs7oa0j.mongodb.net/?retryWrites=true&w=majority"
def get_latest_file_content():
    client = MongoClient(uri)
    db = client['Inscribd']
    collection = db['Files']
    latest_file = collection.find_one(sort=[('_id', -1)])
    if latest_file:
        file_content = latest_file.get('file_content')
        if file_content:
            return file_content
    else:
        return None
    client.close()
def home():
    st.title("Welcome to Inscribd")
def lectures():
    st.title("Lectures")
    st.markdown("## Transcription")
    st.write(get_latest_file_content())
pages = {
    "Home": home,
    "Lectures": lectures,
}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[selection]
page()
