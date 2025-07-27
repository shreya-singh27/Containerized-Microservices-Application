from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "User Service is running"

@app.route('/users')
def get_users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

