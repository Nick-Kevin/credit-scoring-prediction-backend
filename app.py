from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable the react front app to access this API

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
