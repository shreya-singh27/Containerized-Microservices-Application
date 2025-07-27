from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Data Service is running"

@app.route('/data')
def get_data():
    return jsonify([
        {"id": 101, "type": "info"},
        {"id": 102, "type": "stat"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

