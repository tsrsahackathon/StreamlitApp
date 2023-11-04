from pymongo import MongoClient
import streamlit as st
import json

uri = "mongodb+srv://shriteqhackathon:5F5RZ96CiqZY4jzM@hackathon.vs7oa0j.mongodb.net/?retryWrites=true&w=majority"


def connect_to_mongodb():
    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Access the database and collection
    db = client['Inscribd']
    collection = db['Files']

    return client, collection


def disconnect_from_mongodb(client):
    # Close the MongoDB client connection
    client.close()


def quiz():
    client, collection = connect_to_mongodb()

    # Find the latest document by sorting based on the '_id' field in descending order and limit to 1 result
    latest_file = collection.find_one(sort=[('_id', -1)])

    if latest_file:
        # Retrieve and return the content of the latest file
        file_content = latest_file.get('file_content')
        if file_content:
            disconnect_from_mongodb(client)
            return file_content

    disconnect_from_mongodb(client)
    return None


def keywords():
    client, collection = connect_to_mongodb()

    # Find the 2nd latest document by sorting based on the '_id' field in descending order and skip 1 result
    second_latest_file = collection.find_one(sort=[('_id', -1)], skip=1)

    if second_latest_file:
        # Retrieve and return the content of the 2nd latest file
        file_content = second_latest_file.get('file_content')
        if file_content:
            disconnect_from_mongodb(client)
            return file_content

    disconnect_from_mongodb(client)
    return None


def summary():
    client, collection = connect_to_mongodb()

    # Find the 3rd latest document by sorting based on the '_id' field in descending order and skip 2 results
    third_latest_file = collection.find_one(sort=[('_id', -1)], skip=2)

    if third_latest_file:
        # Retrieve and return the content of the 3rd latest file
        file_content = third_latest_file.get('file_content')
        if file_content:
            disconnect_from_mongodb(client)
            return file_content

    disconnect_from_mongodb(client)
    return None


def transcription():
    client, collection = connect_to_mongodb()

    # Find the 4th latest document by sorting based on the '_id' field in descending order and skip 3 results
    fourth_latest_file = collection.find_one(sort=[('_id', -1)], skip=3)

    if fourth_latest_file:
        # Retrieve and return the content of the 4th latest file
        file_content = fourth_latest_file.get('file_content')
        if file_content:
            disconnect_from_mongodb(client)
            return file_content

    disconnect_from_mongodb(client)
    return None


#######################
st.set_page_config(page_title="Inscribd",
                   page_icon="your_logo.png", initial_sidebar_state="expanded")


def home():
    st.title("Welcome to")

    # Add a logo
    logo = st.image("your_logo.png", use_column_width=True)

    # Style the home page
    st.markdown(
        """
        <style>
            .stMarkdown {
                font-size: 24px;
                line-height: 1.6;
                text-align: center;
                margin: 20px 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def quizdisplay():
    quiz_data = json.loads(quiz())

    for i, question_data in enumerate(quiz_data["multiple_choice"]):
        st.header(f"Question {i + 1}: {question_data['question']}")
        for j, answer in enumerate(question_data['answers']):
            clicked = st.button(f"Option {chr(65 + j)}: {answer['option']}")
            if clicked and answer['correct']:
                st.write("Correct!")
            elif clicked and not answer['correct']:
                st.write("Incorrect.")


def lectures():
    st.title("Lectures")

    # Create tabs for Transcription, Summary, Keywords, and Quiz
    selected_tab = st.selectbox(
        "Select a tab:", ["Transcription", "Summary", "Keywords", "Quiz"])

    if selected_tab == "Transcription":
        st.markdown("## Transcription")
        st.write(transcription())
    elif selected_tab == "Summary":
        st.markdown("## Summary")
        st.write(summary())
    elif selected_tab == "Keywords":
        st.markdown("## Keywords")
        st.write(keywords())
    elif selected_tab == "Quiz":
        st.markdown("## Quiz")
        quizdisplay()


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

#######################
