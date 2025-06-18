<<<<<<< HEAD
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = 'http://localhost:9000'  # Adjust this if your backend runs on a different port

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    form_data = dict(request.form)  # Now this will work
    response = requests.post(f'{BACKEND_URL}/signup', json=form_data)
    return response.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
=======
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = 'http://localhost:9000'  # Adjust this if your backend runs on a different port

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    form_data = dict(request.form)  # Now this will work
    response = requests.post(f'{BACKEND_URL}/signup', json=form_data)
    return response.text

@app.route('/update', methods=['POST'])
def update():
    form_data = dict(request.form)
    response = requests.post(f'{BACKEND_URL}/update', json=form_data)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
>>>>>>> af418ba (Assignment 5)
