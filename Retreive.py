from pymongo import MongoClient

uri = "mongodb+srv://shriteqhackathon:5F5RZ96CiqZY4jzM@hackathon.vs7oa0j.mongodb.net/?retryWrites=true&w=majority"


def get_latest_file_content():
    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Access the database and collection
    db = client['Inscribd']
    collection = db['Files']

    # Find the latest document by sorting based on the '_id' field in descending order and limit to 1 result
    latest_file = collection.find_one(sort=[('_id', -1)])

    if latest_file:
        # Retrieve and return the content of the latest file
        file_content = latest_file.get('file_content')
        if file_content:
            return file_content
    else:
        return None

    client.close()
