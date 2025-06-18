<<<<<<< HEAD
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    day = datetime.now().strftime('%A')
    return render_template('index.html', day=day)

@app.route('/api', methods=['POST'])
def route_name():
    name = request.form.get('name')
    age = request.form.get('age')

    return render_template(
        'index.html',
        day=datetime.now().strftime('%A'),
        name=name,
        age=age,
        message=f'Hello {name}, you are {age} years old!'
    )

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    day = datetime.now().strftime('%A')
    return render_template('index.html', day=day)

@app.route('/api', methods=['POST'])
def route_name():
    name = request.form.get('name')
    age = request.form.get('age')

    return render_template(
        'index.html',
        day=datetime.now().strftime('%A'),
        name=name,
        age=age,
        message=f'Hello {name}, you are {age} years old!'
    )

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> af418ba (Assignment 5)
