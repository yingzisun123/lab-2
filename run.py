from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return 'Current Time: ' + current_time

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
