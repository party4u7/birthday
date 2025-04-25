from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    if name:
        with open('names.txt', 'a', encoding='utf-8') as f:
            f.write(name + '\n')
        return 'OK', 200
    return 'Bad Request', 400

if __name__ == '__main__':
    app.run(debug=True)
