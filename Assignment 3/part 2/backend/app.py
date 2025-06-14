from flask import Flask, request
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import jsonify

load_dotenv()  # Ensure environment variables are loaded

# Create a new client and connect to the server
client = MongoClient(os.getenv("MONGO_URI"))

db = client.test_db
collection = db.test_collection

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
@app.route('/signup', methods=['POST'])
def signup():
    form_data = request.json  # ✅ Get JSON payload
    collection.insert_one(form_data)
    return 'success'


 
@app.route('/view')
def get_data():
    data_cursor = collection.find()

    data_list = []
    for item in data_cursor:
        item.pop('_id', None)  # Remove MongoDB's ObjectId (not JSON serializable)
        data_list.append(item)

    return jsonify({'data': data_list})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
